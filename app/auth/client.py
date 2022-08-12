#!/bin/python3

from http import HTTPStatus
from getpass import getpass
import requests
from datetime import datetime
import json
import sys
from logger import Logger
from users import UserStorage

def ExecuteRequest(method, url, headers):
    Logger.Info(f">>> [{method}] {url} -> Headers: {headers}")
    response = requests.request(method=method, url=url, headers=headers)
    msg = f"<<< [{method}] Respose: {HTTPStatus(response.status_code).name}:{response.status_code}\n Headers:\n\t{response.headers}\n\n Body:\n\t{json.dumps(response.json())}"
    
    if response.status_code == HTTPStatus.OK:
        Logger.Success(msg)
    else:
        Logger.Error(msg)

    return response      


print(f"Knowed users: { json.dumps(UserStorage.Users, indent=4, sort_keys=True) }")
user =  input("User: ")
password = getpass()

response = ExecuteRequest('POST', f"http://localhost:5000/login", { 'user': user, 'pass': password })

if response.status_code != HTTPStatus.OK:
    Logger.Error(f"Login request fail -> {response.status_code}")
    sys.exit()

token = response.json()['token']

Logger.Info(f"\n##\n##\n## Authenticated, validating token {token}\n##\n##")

response = ExecuteRequest('POST', f"http://localhost:5000/validate", headers={ 'token': token })