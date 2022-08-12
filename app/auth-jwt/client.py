#!/bin/python3

from http import HTTPStatus
import json
import time
import sys
from getpass import getpass
from datetime import datetime, timedelta
from cripto import CriptoClient
import jwt
from logger import Logger
from requester import Requester
from users import UserStorage

# class to handle with asymmetric keys, in client side
cripto = CriptoClient()

print(f"Knowed users: { json.dumps(UserStorage.Users, indent=4, sort_keys=True) }")
user =  input("User: ")
password = getpass()

url = "http://localhost:5000/login"

# Try login
result = Requester.Execute('POST', url, { 'requestToken': cripto.Encript(json.dumps({ 'user': user, 'pass' : password }))})

if result['status_code'] != HTTPStatus.OK:
    Logger.Error("### Auth error")
    sys.exit()

token = result['jwt']
claims = jwt.decode(token, key=cripto.GetPublicKey(), algorithms=[ 'RS256', ], options={"verify_signature": True, "verify_exp": True})
exp = datetime.fromtimestamp(result['exp'])+timedelta(seconds=2)

Logger.Info(f"\n##\n##\n##\tRoutes allowed for this user: {claims['routes']}\n##\n##")

#Timeout/Expire Token test
Logger.Info(f"Trying all routes {claims['routes']} util {datetime.now()}/{exp} time out not arrive -> to test token expiration")
while datetime.now() < exp:
    timeOut = (datetime.fromtimestamp(result['exp']) - datetime.now()).total_seconds()
    if timeOut < 0:
        Logger.Info("Token time out, next requests will be the last...")
        time.sleep(1)
    else:
        Logger.Info(f"Time to expire: {timeOut} seconds, continue trying until expire token")


    for r in claims['routes']:
        Requester.Execute('GET', f"http://localhost:5000/{r}", { 'Authorization': f"Bearer {token}" })

    time.sleep(1)

