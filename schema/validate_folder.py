#!/usr/bin/python3
# Author: Alexis Boni
# SPDX-License-Identifier: AGPL-3.0-or-later

"""
Validate all files in a folder against a schema file.
"""
import glob
import sys
import argparse
import validate_schema


def main(args=None):
    """
    Validate all files in a folder against a schema file.
    """

    extension = 'json' if args.json else 'y*ml'
    path = f'{args.folder}/*.{extension}'

    for file in glob.glob(path, recursive=args.recursive):
        print(file)
        validate_schema.main(file, args.schema, args.json)

    print(f'\n [OK] Validation success for folder: {args.folder}')

    return 0


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument(
        '-f', '--folder',
        help="Folder with files to validate.",
        required=True
    )
    argument_parser.add_argument(
        '-j', '--json',
        help="Use a JSON file as source instead of YAML", action='store_true',
    )
    argument_parser.add_argument(
        '-s', '--schema',
        help="Schema file to validate against.",
        required=True
    )
    argument_parser.add_argument(
        '-r', '--recursive',
        help="Validate recursively",
        action='store_true'
    )
    arguments = argument_parser.parse_args()
    sys.exit(main(arguments) or 0)
