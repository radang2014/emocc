# emoc_to_c.py
#
# Reads in an Emo-C program (file name passed on command line), transpiles
# it to C, and prints the resulting C program to stdout
#
# Written by: Randy Dang, October 2024

import os
import sys
import load_emoc_mappings as lem

EXIT_FAILURE = 1

PROGRAM_FILENAME = os.path.basename(__file__)

# Read entire Emo-C program from source file and return contents
def read_emo_program(emo_filename):
    emo_program = None
    with open(emo_filename, "r") as emo_file:
        emo_program = emo_file.read()
    return emo_program

# Transpile Emo-C program to C and return contents of C program
def transpile_emo_program(emo_program):
    mappings, escape_char, escape_mappings = lem.load_emoc_mappings()

    c_program = ""
    inside_char = False
    inside_string = False
    escape = False
    for emo_char in emo_program:
        # If character is escape character within a string, set state
        # accordingly and do NOT include in output
        if not escape and (inside_string or inside_char) and \
           emo_char == escape_char:
            escape = True
            continue

        # Error checking: if in escape state, next character MUST complete
        # an escape sequence
        if escape:
            if emo_char not in escape_mappings:
                raise Exception(f"ERROR: Escape character '{escape_char}' " +
                                f"is followed by a '{emo_char}' character, " +
                                f"which does not complete an escape " +
                                f"sequence. This is syntactically invalid.")

        # Exit character upon encountering closed single quote character
        closed_single_quote = False
        if not escape and inside_char and emo_char in mappings and \
           mappings[emo_char] == "'":
            inside_char = False
            closed_single_quote = True

        # Exit string upon encountering closed quote character
        closed_quote = False
        if not escape and inside_string and emo_char in mappings and \
           mappings[emo_char] == "\"":
            inside_string = False
            closed_quote = True

        # Find C token corresponding to Emo-C character if one exists, or
        # escape sequence if applicable
        if emo_char in mappings and not (inside_string or inside_char):
            c_program += mappings[emo_char]
        elif escape and (inside_string or inside_char):
            c_program += escape_mappings[emo_char]
        else:
            c_program += emo_char

        # Enter character upon encountering open single quote character
        if not inside_char and not closed_single_quote and \
           emo_char in mappings and mappings[emo_char] == "'":
            inside_char = True

        # Enter string upon encountering open quote character
        if not inside_string and not closed_quote and emo_char in mappings and \
           mappings[emo_char] == "\"":
            inside_string = True

        escape = False

    return c_program

# Write c program to stdout
def write_c_program(c_program):
    sys.stdout.write(c_program)

def main(emo_filename):
    emo_program = read_emo_program(emo_filename)
    c_program = transpile_emo_program(emo_program)
    write_c_program(c_program)

if __name__ == "__main__":
    # Process command line arguments
    if len(sys.argv) < 2:
        sys.stderr.write(f"Usage: python {PROGRAM_FILENAME} <emo_filename>\n")
        exit(EXIT_FAILURE)

    main(sys.argv[1])
