#!/usr/bin/python3
# Author: Alexis Boni
# SPDX-License-Identifier: AGPL-3.0-or-later

"""
Gets the latest JSON schema from flosstudio repository.
"""

import sys
import json
import argparse
import requests


def main(args=None):
    """
    Gets the latest JSON schema from flosstudio repository.
    """

    releases_repository = "https://api.github.com/repos/flosstudio/schema/releases/latest"
    asset_name = "flosstudio.schema.json"

    # Get latest release url
    res = requests.get(releases_repository)

    if not res:
        print(f'Error fetching releases repository: {res.status_code}')
        return 1

    assets = res.json()['assets']

    schema_url = next((x for x in assets if x['name'] == asset_name), None)
    if schema_url is None:
        print(f'Releases Name not found: {asset_name}')
        return 1

    schema_entry = schema_url['browser_download_url']
    file_res = requests.get(schema_entry)
    if not file_res:
        print(f'Error fetching schema release: {res.status_code}')
        return 1

    # Download the file
    if args is not None and args.file:
        with open(args.file, 'wb') as dst_file:
            dst_file.write(file_res.content)
    else:
        if(args is not None and args.human):
            json.dump(file_res.json(), sys.stdout, indent=2)
        else:
            return file_res.json()


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument(
        '-f', '--file',
        help="Save to file ", nargs='?', const='flosstudio.schema.json'
    )
    argument_parser.add_argument(
        '-u', '--human',
        action='store_true',
        help="Output a readable formatted json to stdout."
    )
    arguments = argument_parser.parse_args()
    sys.exit(main(arguments) or 0)
