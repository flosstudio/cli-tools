#!/usr/bin/python3

# Author: Fabio Pesari
# SPDX-License-Identifier: AGPL-3.0-or-later

"""
Downloads the JSON SPDX license list, filters it and converts it to YAML
"""

import json
import requests
import yaml

SPDX_JSON = 'https://raw.githubusercontent.com/spdx/license-list-data/master/json/licenses.json'

licenses = json.loads(requests.get(SPDX_JSON).text)['licenses']

output = yaml.dump(
    [i['licenseId'] for i in licenses
     if i.get('isOsiApproved') or i.get('isFsfLibre')])

print(output)
