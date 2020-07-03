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
    argument_parser = argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument(
        '-f', '--file',
        help="Save to file ", nargs='?', const='flosstudio.schema.json'
    )

    args = argument_parser.parse_args(args)

    releases_repository = "https://api.github.com/repos/flosstudio/schema/releases/latest"
    asset_name = "flosstudio.schema.json"

    # Get latest release url
    res = requests.get(releases_repository)
    assets = res.json()['assets']
    schema_url = next(x for x in assets if x['name'] == asset_name)[
        'browser_download_url']

    # Download the file
    file_res = requests.get(schema_url)

    if args.file:
        with open(args.file, 'wb') as dst_file:
            dst_file.write(file_res.content)
    else:
        json.dump(file_res.json(), sys.stdout, indent=2)


if __name__ == '__main__':
    sys.exit(main() or 0)
