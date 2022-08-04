#!/bin/python3

import requests
import json

body = {}
body["name"] = input("Type your name: ")

response = requests.post(f"http://localhost:5000", json = body)

print(response.json())
