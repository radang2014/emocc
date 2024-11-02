# format_md_table.py
#
# Formats markdown tables and individual cells according to provided
# data.
#
# This is meant to be an imported module, NOT to be run as a main
# script.
#
# Written by: Randy Dang, November 2024

import os
import sys

EXIT_FAILURE = 1

PROGRAM_FILENAME = os.path.basename(__file__)

# Creates Markdown table according to provided headings and data.
# Formatter functions are callbacks to functions that provide
# any special formatting
# The width of each heading is assumed to be the minimum width of
# the corresponding column in the Markdown code.
def format_md_table(headings, data_rows, formatter_funcs=None):
    heading_lens = [len(heading) for heading in headings]

    # Default formatter function
    def default_formatter(value, length):
        return str(value).ljust(length)

    # Set to default formatter if no formatter function provided
    if formatter_funcs == None:
        formatter_funcs = [default_formatter for _ in headings]
    for formatter_func_idx, formatter_func in enumerate(formatter_funcs):
        if formatter_func == None:
            formatter_funcs[formatter_func_idx] = default_formatter

    table = ""

    # Write Table Header
    table += "|"
    for heading in headings:
        table += f" {heading} " + "|"
    table += "\n"

    table += "|"
    for heading_len in heading_lens:
        table += "-" + ("-" * heading_len) + "-|"
    table += "\n"

    # Write Table Rows
    first_row = True
    for data_row in data_rows:
        if not first_row:
            table += "\n"

        # Write Table Row for current row of data
        table += "|"
        for data_cell, heading_len, formatter_func in \
            zip(data_row, heading_lens, formatter_funcs):

            # Write current cell in row
            data_cell_formatted = formatter_func(data_cell, heading_len)
            table += " " + data_cell_formatted + " |"

        first_row = False

    return table

# The following functions format the indicated data value according to
# the desired format within a Markdown table cell, widened to the
# indicated length

def format_c_token(value, length):
    formatted = None

    # Exception cases where we don't want the literal character inserted
    # in the table
    if value == "\n":
        formatted = "(newline character)"
    elif value == " ":
        formatted = "(space character)"
    # Default case
    else:
        # Handle edge case characters
        value = value.replace("`", " ` ")
        value = value.replace("|", "\\|")

        formatted = f"``{value}``"

    return formatted.ljust(length)

def format_emo_char(value, length):
    return value + (" " * (length - 1))

def format_emo_char_pair(value, length):
    return value + (" " * (length - 2))

def format_emo_unicode(value, length):
    # Compute numerical value for each component of emoji
    unicode_components = [
        ord(emo_char_component) for emo_char_component in value
    ]

    # Format numerical components as unicode hex
    formatted_components = [
        f"U+{emo_unicode_component:X}" \
        for emo_unicode_component in unicode_components
    ]

    formatted = " ".join(formatted_components)
    return formatted.ljust(length)

if __name__ == "__main__":
    sys.stderr.write(f"ERROR: File {PROGRAM_FILENAME} does not have a main " +
                     f"script but was run as if it did.\n")
    exit(EXIT_FAILURE)

