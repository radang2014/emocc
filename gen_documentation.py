# gen_documentation.py
#
# Reads in a documentation source file (passed on the command line) and replaces
# all instances of `<!-- GENERATE: ... -->` with code output as defined
# in this file. Prints the resulting documentation file to stdout.

import os
import sys
import load_emoc_mappings as lem
import format_md_table as fmt

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
        "gen_single_quote_char" : gen_single_quote_char,
        "gen_escape_char" : gen_escape_char,
        "gen_escape_mappings" : gen_escape_mappings
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
    mappings, _, _ = lem.load_emoc_mappings()
    headings = ["C Keyword or Symbol", "Emo-C Character",
                "Unicode Hex Value "]
    formatter_funcs = [
        fmt.format_c_token, fmt.format_emo_char, fmt.format_emo_unicode
    ]

    # Extract table data from JSON file
    data = list()
    for emo_char in mappings:
        c_token = mappings[emo_char]
        data.append([c_token, emo_char, emo_char])

    return fmt.format_md_table(headings, data, formatter_funcs)

# Returns Emo-C character corresponding to a C quotation mark
def gen_quote_char():
    mappings, _, _ = lem.load_emoc_mappings()
    return lem.get_emo_from_c(mappings, "\"")

# Returns Emo-C character corresponding to a C single quotation mark
def gen_single_quote_char():
    mappings, _, _ = lem.load_emoc_mappings()
    return lem.get_emo_from_c(mappings, "'")

# Returns Emo-C escape character used in strings
def gen_escape_char():
    _, escape_char, _ = lem.load_emoc_mappings()
    return escape_char

# Creates Markdown table of Emo-C escape sequences and corresponding
# characters based on JSON data file
def gen_escape_mappings():
    _, escape_char, mappings = lem.load_emoc_mappings()
    headings = [
        "Emo-C Escape Sequence",
        "Unicode Hex Value (not including escape character)", 
        "C character      "
    ]
    formatter_funcs = [
        fmt.format_emo_char_pair, fmt.format_emo_unicode, fmt.format_c_token
    ]

    # Extract table data from JSON file
    data = list()
    for escape_sequence_key in mappings:
        escape_sequence = escape_char + escape_sequence_key
        c_char = mappings[escape_sequence_key]
        data.append([escape_sequence, escape_sequence_key, c_char])

    return fmt.format_md_table(headings, data, formatter_funcs)

# Adds generated components to documentation and returns resulting contents
def add_generated_components(doc_src_file):
    for gen_key in GENERATE_FUNC_MAPPINGS:
        doc_src_file = doc_src_file.replace(get_doc_src_value(gen_key),
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

