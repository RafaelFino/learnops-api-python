#!/bin/python3

import requests

response = requests.get('http://localhost:5000/')

print(response.json())