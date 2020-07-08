#!/usr/bin/python3
# Author: Alexis Boni
# SPDX-License-Identifier: AGPL-3.0-or-later

"""
Validate a JSON/YAML file against a schema file.
"""

import sys
import json
import argparse
import yaml
import jsonschema


def main(file, schema, json_flag):
    """
    Validate a YAML/JSON file against a schema file.
    """
    schema = open(schema, 'r').read()
    schema_contents = json.loads(schema)
    raw_file = open(file, 'r')
    file_contents = raw_file.read()

    #  If we get a yaml file convert it to json.
    if not json_flag:
        file_contents = yaml.load(file_contents, Loader=yaml.FullLoader)

    jsonschema.validate(instance=file_contents, schema=schema_contents)

    print(f'[OK] Validation success for {file}')

    return 0


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument(
        '-j', '--json',
        help="Use a JSON file as source instead of YAML", action='store_true',
    )
    argument_parser.add_argument(
        '-f', '--file',
        help="YAML/JSON File to validate.",
        required=True
    )
    argument_parser.add_argument(
        '-s', '--schema',
        help="Schema file to validate against.",
        required=True
    )
    arguments = argument_parser.parse_args()
    sys.exit(main(arguments.file, arguments.schema, arguments.json) or 0)
