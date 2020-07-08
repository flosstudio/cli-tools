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
import get_schema
import jsonschema


def main(args=None):
    """
    Validate a YAML/JSON file against a schema file.
    """

    raw_file = open(args.file, 'r')
    parsed_file = raw_file.read()

    #  If we get a yaml file convert it to json.
    if not args.json:
        parsed_file = yaml.load(parsed_file, Loader=yaml.FullLoader)

    schema = get_schema.main(args=None)
    jsonschema.validate(instance=parsed_file, schema=schema)
    print(f'[OK] Validation success for {args.file}')

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
    arguments = argument_parser.parse_args()
    sys.exit(main(arguments) or 0)
