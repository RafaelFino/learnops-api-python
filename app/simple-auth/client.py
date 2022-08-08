#!/bin/python3

from http import HTTPStatus
import sys
import requests
import json

def tryParseInt(s, base=10, val=None):
    try:
        return int(s, base)
    except ValueError:
        return val 

body = {}
user =  input("User: ")
password = input("Password: ")

print(f"trying to get a token from user {user}...")
response = requests.post(f"http://localhost:5000/login", headers={ 'user': user, 'pass': password })

print(f"Return:\nReturn code: {response.status_code}\nBody:{json.dumps(response.json(), indent=4, sort_keys=True)}")

if response.status_code != HTTPStatus.OK:    
    print("Fail to try login")
    sys.exit()

token = response.json()['token']
print(f"Authenticaed, validating token {token}")

response = requests.post(f"http://localhost:5000/validate", headers={ 'token': token })

print(f"Return:\nReturn code: {response.status_code}\nBody:{json.dumps(response.json(), indent=4, sort_keys=True)}")

