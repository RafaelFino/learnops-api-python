#!/bin/python3

import requests
import json

response = requests.get('http://localhost:5000/')

print(json.dumps(response.json(), indent=4, sort_keys=True))