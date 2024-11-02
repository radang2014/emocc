# load_emoc_mappings.py
#
# Loads JSON file containing mapping between Emo-C characters and C
# keywords/symbols, and returns object(s) containing that information
#
# This is meant to be an imported module, NOT to be run as a main
# script.
#
# Written by: Randy Dang, October 2024

import json
import os
import sys

EXIT_FAILURE = 1

PROGRAM_FILENAME = os.path.basename(__file__)
EMO_TO_C_MAPPINGS_FILENAME = "emoc_to_c.json";

# Load emoji mappings from JSON configuration
def load_emoc_mappings():
    config = None
    with open(EMO_TO_C_MAPPINGS_FILENAME, "r") as config_file:
        config = json.load(config_file,
                           object_pairs_hook=validate_emoc_mappings)
    return config["mappings"], config["escape_char"], config["escape_mappings"]

# Ensure there are no duplicate keys in mappings; otherwise, raise exception
def validate_emoc_mappings(mapping_pairs):
    mappings = dict()
    for key, value in mapping_pairs:
        if key in mappings:
            raise Exception(f"Duplicate emoji in mappings: {key}")
        mappings[key] = value
    return mappings

# Given C keyword or symbol, return corresponding emoji. Return None if no
# such emoji exists.
def get_emo_from_c(mappings, c_token):
    for emo_char in mappings:
        if mappings[emo_char] == c_token:
            return emo_char
    return None

if __name__ == "__main__":
    sys.stderr.write(f"ERROR: File {PROGRAM_FILENAME} does not have a main " +
                     f"script but was run as if it did.\n")
    exit(EXIT_FAILURE)

