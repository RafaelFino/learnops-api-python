#!/bin/python3

import requests
import json

def tryParseInt(s, base=10, val=None):
    try:
        return int(s, base)
    except ValueError:
        return val 

body = {}
body["numbers"] = []

typed = input("Type a number (or empty to finish): ")

while len(typed) > 0:
    newItem = tryParseInt(typed)
    if newItem != None:
        body["numbers"].append(newItem)
    else:
        break

    typed = input("Next number or empty to finish: ")

response = requests.post(f"http://localhost:5000/sum", json = body)

print(json.dumps(response.json(), indent=4, sort_keys=True))