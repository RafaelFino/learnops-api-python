#!/bin/python3

from http import HTTPStatus
from getpass import getpass
import requests
from datetime import datetime
import json
import sys


# Background Colors to log messages
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def Log(message):
    print(f"{bcolors.BOLD}{bcolors.OKBLUE}[{datetime.now()}] {bcolors.OKCYAN}{message}")

def LogError(message):
    print(f"{bcolors.BOLD}{bcolors.OKBLUE}[{datetime.now()}] {bcolors.FAIL}{message}")

def LogOk(message):
    print(f"{bcolors.BOLD}{bcolors.OKBLUE}[{datetime.now()}] {bcolors.OKGREEN}{message}") 

def ExecuteRequest(method, url, headers):
    Log(f">>> [{method}] {url} -> Headers: {headers}")
    response = requests.request(method=method, url=url, headers=headers)
    msg = f"<<< [{method}] Respose: {HTTPStatus(response.status_code).name}:{response.status_code}\n Headers:\n\t{response.headers}\n\n Body:\n\t{json.dumps(response.json())}"
    
    if response.status_code == HTTPStatus.OK:
        LogOk(msg)
    else:
        LogError(msg)

    return response      

user =  input("User: ")
password = getpass()

response = ExecuteRequest('POST', f"http://localhost:5000/login", { 'user': user, 'pass': password })

if response.status_code != HTTPStatus.OK:
    LogError(f"Login request fail -> {response.status_code}")
    sys.exit()

token = response.json()['token']

Log(f"\n##\n##\n## Authenticated, validating token {token}\n##\n##")

response = ExecuteRequest('POST', f"http://localhost:5000/validate", headers={ 'token': token })