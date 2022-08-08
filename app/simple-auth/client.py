#!/bin/python3

from http import HTTPStatus
import sys
import requests
import json
from getpass import getpass

user =  input("User: ")
password = getpass()

headers={ 'user': user, 'pass': password }

print(f"trying to get a token from user {user} -> header={headers}")
response = requests.post(f"http://localhost:5000/login", headers)
print(f"Return:\nReturn code: {response.status_code}\nBody:{json.dumps(response.json(), indent=4, sort_keys=True)}")

if response.status_code != HTTPStatus.OK:    
    print("Fail to try login")
    sys.exit()

token = response.json()['token']
print(f"Authenticated, validating token {token}")

response = requests.post(f"http://localhost:5000/validate", headers={ 'token': token })
print(f"####\nReturn:\nReturn code: {response.status_code}\nBody:{json.dumps(response.json(), indent=4, sort_keys=True)}")

