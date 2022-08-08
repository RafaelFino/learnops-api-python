#!/bin/python3

from http import HTTPStatus
import sys
import requests
import json
from getpass import getpass
from datetime import datetime

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
    Log(f">>> [{method}] {url} -> {headers}")
    response = requests.request(method=method, url=url, headers=headers)
    if response.status_code == HTTPStatus.OK:
        LogOk(f"<<< HTTPCode: {response.status_code}:{json.dumps(response.json(), indent=4, sort_keys=True)}")
    else:
        LogError(f"<<< HTTPCode: {response.status_code}:{json.dumps(response.json(), indent=4, sort_keys=True)}")    
        sys.exit()        

    return response.json()

user =  input("User: ")
password = getpass()

headers={ 'user': user, 'pass': password }
url = "http://localhost:5000/login"

response = ExecuteRequest('POST', url, headers)

jwt = response['jwt']

# try admin get
ExecuteRequest('GET',"http://localhost:5000/admin", { 'Authorization': f"Bearer {jwt}" })

# try query get
ExecuteRequest('GET',"http://localhost:5000/query", { 'Authorization': f"Bearer {jwt}" })


