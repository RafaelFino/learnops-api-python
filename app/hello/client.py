#!/bin/python3

import requests

name = input("Type your name: ")

response = requests.get(f"http://localhost:5000/hello/{name}")

print(response.json())