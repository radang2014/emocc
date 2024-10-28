# gen_documentation.py
#
# Reads in a documentation source file (passed on the command line) and replaces
# all instances of `<!-- GENERATE: ... -->` with code output as defined
# in this file. Prints the resulting documentation file to stdout.

import os
import sys
import load_emoc_mappings as lem

EXIT_FAILURE = 1

PROGRAM_FILENAME = os.path.basename(__file__)

HELLO_WORLD_FILENAME = "hello_world.emoc"

# Initialize global mappings from generation key to generation function
def init_generate_func_mappings():
    global GENERATE_FUNC_MAPPINGS
    GENERATE_FUNC_MAPPINGS = {
        "gen_hello_world" : gen_hello_world,
        "gen_language_specification" : gen_language_specification,
        "gen_quote_char" : gen_quote_char,
        "gen_escape_char" : gen_escape_char
    }

# Reads entire documentation source file and returns contents
def read_doc_src_file(doc_src_filename):
    doc_src = None
    with open(doc_src_filename, "r") as doc_src_file:
        doc_src = doc_src_file.read()
    return doc_src

# Returns string that would appear in documentation source file based on
# inputted generation key
def get_doc_src_value(gen_key):
    return f"<!-- GENERATE: {gen_key} -->"

# Returns contents of last line of example "Hello World" program
def gen_hello_world():
    hello_world_program = None
    with open(HELLO_WORLD_FILENAME, "r") as hello_world_file:
        hello_world_program = hello_world_file.readlines()[-1]
    return hello_world_program

# Creates Markdown table of C to Emo-C mappings based on JSON data file
def gen_language_specification():
    mappings, _ = lem.load_emoc_mappings()
    headings = ["C Keyword or Symbol", "Emo-C Character", \
                "Unicode Hex Value "]
    heading_lens = [len(heading) for heading in headings]

    # Formatter functions for each column of table

    def format_c_token(c_token, length):
        formatted = None

        # Exception cases where we don't want the literal character inserted
        # in the table
        if c_token == "\n":
            formatted = "(newline character)"
        elif c_token == " ":
            formatted = "(space character)"
        # Default case
        else:
            formatted = f"`{c_token}`"

        return formatted.ljust(length)

    def format_emo_char(emo_char, length):
        return emo_char + (" " * (length - 1))

    def format_emo_unicode(emo_unicode, length):
        # Format numerical components of emoji as unicode hex
        formatted_components = [
            f"U+{emo_unicode_component:X}" \
            for emo_unicode_component in emo_unicode
        ]

        formatted = " ".join(formatted_components)
        return formatted.ljust(length)

    formatter_funcs = [format_c_token, format_emo_char, format_emo_unicode]

    language_spec = ""

    # Write Table Header
    language_spec += "|"
    for heading in headings:
        language_spec += f" {heading} " + "|"
    language_spec += "\n"

    language_spec += "|"
    for heading_len in heading_lens:
        language_spec += "-" + ("-" * heading_len) + "-|"
    language_spec += "\n"

    # Write Table Rows
    first_row = True
    for emo_char in mappings:
        if not first_row:
            language_spec += "\n"

        # Write Table Row for current mapping
        c_token = mappings[emo_char]
        emo_unicode = [ # compute numerical value for each component of emoji
            ord(emo_char_component) for emo_char_component in emo_char
        ]
        row_values = [c_token, emo_char, emo_unicode]

        language_spec += "|"
        for row_value, heading_len, formatter_func in \
            zip(row_values, heading_lens, formatter_funcs):

            # Write current cell in row
            row_value_formatted = formatter_func(row_value, heading_len)
            language_spec += " " + row_value_formatted + " |"

        first_row = False

    return language_spec

def gen_quote_char():
    mappings, _ = lem.load_emoc_mappings()
    return lem.get_emo_from_c(mappings, "\"")

def gen_escape_char():
    _, escape_char = lem.load_emoc_mappings()
    return escape_char

# Adds generated components to documentation and returns resulting contents
def add_generated_components(doc_src_file):
    for gen_key in GENERATE_FUNC_MAPPINGS:
        doc_src_file = doc_src_file.replace(get_doc_src_value(gen_key), \
                                            GENERATE_FUNC_MAPPINGS[gen_key]())
    return doc_src_file

# Write generated documentation to stdout
def write_doc_file(doc_file):
    sys.stdout.write(doc_file)

def main(doc_src_filename):
    init_generate_func_mappings()
    doc_src_file = read_doc_src_file(doc_src_filename)
    doc_file = add_generated_components(doc_src_file)
    write_doc_file(doc_file)

if __name__ == "__main__":
    # Process command line arguments
    if len(sys.argv) < 2:
        sys.stderr.write(f"Usage: python {PROGRAM_FILENAME} " +
                         f"<doc_src_filename>\n")
        exit(EXIT_FAILURE)

    main(sys.argv[1])

