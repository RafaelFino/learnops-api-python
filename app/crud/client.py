#!/bin/python3

from email.policy import HTTP
from http import HTTPStatus
from http.client import NOT_FOUND
import requests
import json
import sys
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

def ExecuteRequest(method, url, body={}):
    Log(f">>> [{method}] {url}: Body: {body}")    
    response = requests.request(method=method, url=url, json=body, headers={'Content-Type': 'application/json'})   
    Log(f"<<< [{method}] Respose: {HTTPStatus(response.status_code).name}:{response.status_code}")

    return response

url = "http://localhost:5000/items"

Log("Trying to get all items")
response = ExecuteRequest('GET', url)
if response.status_code == HTTPStatus.OK:
    LogOk(f"Ok! -> result:\n{json.dumps(response.json())}")
if response.status_code == HTTPStatus.NOT_FOUND:
    LogOk(f"No items yet")

items = {}
qty = 10

for i in range(qty):
    id = f"item{i}"        
    items[id] = {} 
    items[id]['item'] = { f"key{i}" : f"value{i}"  }

    Log(f"Trying to insert items for first time, expecting HTTP 201" )
    response = ExecuteRequest('POST', f"{url}/{id}", items[id])
    if response.status_code == HTTPStatus.CREATED:
        LogOk("Ok!")
    else:
        LogError("Fail!")

    Log(f"Trying to insert an item that already exists, expecting HTTP 200" )
    response = ExecuteRequest('POST', f"{url}/{id}", items[id])
    if response.status_code == HTTPStatus.OK:
        LogOk("Ok!")
    else:
        LogError("Fail!")

Log("Trying to get all items, by ID")
for k in items:    
    response = ExecuteRequest('GET', f"{url}/{k}")
    if response.status_code == HTTPStatus.OK:
        LogOk("Ok!")
    else:
        LogError("Fail!")    


Log("Trying to get a not found item (key = XPTO), expecting HTTP 404")
response = ExecuteRequest('GET', f"{url}/XPTO")
if response.status_code == HTTPStatus.NOT_FOUND:
    LogOk("Ok!")
else:
    LogError("Fail!")

updatedItem = {}

for k in items:
    updatedItem['item'] = { "updated_key": "updated_value" }
    Log(f"Trying to update a item (key={k}) -> new value: {updatedItem}, expecting HTTP 200")
    response = ExecuteRequest('PUT', f"{url}/{k}", updatedItem)
    if response.status_code == HTTPStatus.OK:
        LogOk("Ok!")
    else:
        LogError("Fail!")

Log(f"Trying to update a item with non existent key (key=XPTO) new value: {updatedItem}, expecting HTTP 200")
response = ExecuteRequest('PUT', f"{url}/XPTO", )
if response.status_code == HTTPStatus.NOT_FOUND:
    LogOk("Ok!")
else:
    LogError("Fail!")

for k in items:
    Log(f"Trying to get an updated item (key = {k}), expecting HTTP 200 and value={updatedItem}")
    response = ExecuteRequest('GET', f"{url}/{k}")
    if response.status_code == HTTPStatus.OK:
        LogOk("Ok!")
    else:
        LogError("Fail!")

for k in items:
    Log(f"Trying to delete item (key = {k}) HTTP 200")
    response = ExecuteRequest('DELETE', f"{url}/{k}")
    if response.status_code == HTTPStatus.OK:
        LogOk("Ok!")
    else:
        LogError("Fail!")

    Log(f"Trying to delete item again (key = {k}) HTTP 404")
    response = ExecuteRequest('DELETE', f"{url}/{k}")
    if response.status_code == HTTPStatus.NOT_FOUND:
        LogOk("Ok!")
    else:
        LogError("Fail!")    

Log("Trying to get all items, by ID, expecting 404")
for k in items:    
    response = ExecuteRequest('GET', f"{url}/{k}")
    if response.status_code == HTTPStatus.NOT_FOUND:
        LogOk(f"Ok!")
    else:
        LogError("Fail!")