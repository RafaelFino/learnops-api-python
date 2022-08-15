#!/bin/python3
import requests
import json

name = input("Type your name: ")

response = requests.get(f"http://localhost:5000/hello/{name}")

print(json.dumps(response.json(), indent=4, sort_keys=True))
