#!/bin/python3

import requests
import json

def tryParseFloat(s):
    try:
        return float(s)
    except ValueError:
        return None

body = {}
body['codes'] = []

body['value'] = tryParseFloat(input("Type a value to convert: "))
typed = input("Currency: ")

while len(typed) > 0:    
    body['codes'].append(typed)
    typed = input("Currency (empty to finish): ")

response = requests.post(f"http://localhost:5000/convert", json = body)

print(response.json())