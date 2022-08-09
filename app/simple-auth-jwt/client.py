#!/bin/python3

from http import HTTPStatus
import sys
import requests
import json
import time
from getpass import getpass
from datetime import datetime, timedelta
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import base64
import jwt

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
    if response.status_code == HTTPStatus.OK:
        LogOk(f"<<< HTTPCode: {response.status_code}:{json.dumps(response.json(), indent=4, sort_keys=True)}")
    else:
        LogError(f"<<< HTTPCode: {response.status_code}:{json.dumps(response.json(), indent=4, sort_keys=True)}")    

    return response.json()

login_key = "My secret login key"

def encryptPass(user, password):
    return jwt.encode({ 'user': user, 'pass': password }, login_key, algorithm="HS256")

user =  input("User: ")
password = getpass()

requestToken = encryptPass(user, password)

headers={ 'requestToken': requestToken }
url = "http://localhost:5000/login"

response = ExecuteRequest('POST', url, headers)

jwt = response['jwt']
exp = datetime.fromtimestamp(response['exp'])+timedelta(seconds=2)

#Timeout test
Log(f"Trying util {datetime.now()}/{exp} time out not arrive -> to test token expiration")
while datetime.now() < exp:    
    Log(f"{datetime.now()}/{exp} Trying until expire token")        
    # try admin get
    ExecuteRequest('GET',"http://localhost:5000/admin", { 'Authorization': f"Bearer {jwt}" })

    # try query get
    ExecuteRequest('GET',"http://localhost:5000/query", { 'Authorization': f"Bearer {jwt}" })
    time.sleep(1)

