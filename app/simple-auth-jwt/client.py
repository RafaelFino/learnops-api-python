#!/bin/python3

from http import HTTPStatus
import requests
import json
import time
import sys
from getpass import getpass
from datetime import datetime, timedelta
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
    
    ret = response.json()
    ret['status_code'] = response.status_code
    msg = f"<<< [{method}] Respose: {HTTPStatus(response.status_code).name}:{response.status_code}\n Headers:\n\t{response.headers}\n Body:\n\t{json.dumps(ret)}"
    
    if response.status_code == HTTPStatus.OK:
        LogOk(msg)
    else:
        LogError(msg)
        
    return ret

login_key = "My secret login key"

def encryptPass(user, password):
    return jwt.encode({ 'user': user, 'pass': password }, login_key, algorithm="HS256")

user =  input("User: ")
password = getpass()

requestToken = encryptPass(user, password)

headers={ 'requestToken': requestToken }
url = "http://localhost:5000/login"

result = ExecuteRequest('POST', url, headers)

if result['status_code'] != HTTPStatus.OK:
    LogError("### Auth error")
    sys.exit()

token = result['jwt']
exp = datetime.fromtimestamp(result['exp'])+timedelta(seconds=2)

#Timeout test
Log(f"Trying util {datetime.now()}/{exp} time out not arrive -> to test token expiration")
while datetime.now() < exp:    
    Log(f"{datetime.now()}/{exp} Trying until expire token")        
    # try admin get
    ExecuteRequest('GET',"http://localhost:5000/admin", { 'Authorization': f"Bearer {token}" })

    # try query get
    ExecuteRequest('GET',"http://localhost:5000/query", { 'Authorization': f"Bearer {token}" })
    time.sleep(1)

