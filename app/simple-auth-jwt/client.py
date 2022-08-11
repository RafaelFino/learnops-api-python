#!/bin/python3

from http import HTTPStatus
import requests
import json
import time
import sys
from getpass import getpass
from datetime import datetime, timedelta
from cripto import CriptoClient
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

def ExecuteRequest(method, url, headers={}):
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

cripto = CriptoClient()

def get_claims(token):
	return jwt.decode(token, key=cripto.GetPublicKey(), algorithms=[ 'RS256', ], options={"verify_signature": True, "verify_exp": True})

user =  input("User: ")
password = getpass()

headers={ 'requestToken': cripto.Encript(json.dumps({ 'user': user, 'pass' : password }))}
url = "http://localhost:5000/login"

result = ExecuteRequest('POST', url, headers)

if result['status_code'] != HTTPStatus.OK:
    LogError("### Auth error")
    sys.exit()

token = result['jwt']
claims = get_claims(token)
exp = datetime.fromtimestamp(result['exp'])+timedelta(seconds=2)

Log(f"\n##\n##\n##\tRoutes allowed for this user: {claims['routes']}\n##\n##")

#Timeout test
Log(f"Trying all routes {claims['routes']} util {datetime.now()}/{exp} time out not arrive -> to test token expiration")
while datetime.now() < exp:
    timeOut = (datetime.fromtimestamp(result['exp']) - datetime.now()).total_seconds()
    if timeOut < 0:
        Log("Token time out, next requests will be the last...")
        time.sleep(1)
    else:
        Log(f"Time to expire: {timeOut} seconds, continue trying until expire token")        

    
    for r in claims['routes']:
        ExecuteRequest('GET', f"http://localhost:5000/{r}", { 'Authorization': f"Bearer {token}" })

    time.sleep(1)

