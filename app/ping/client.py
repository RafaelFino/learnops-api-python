#!/bin/python3

import requests

response = requests.get('http://localhost:5000/ping')

print(json.dumps(response.json(), indent=4, sort_keys=True))