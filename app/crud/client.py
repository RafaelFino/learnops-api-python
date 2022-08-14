#!/bin/python3

from email.policy import HTTP
from http import HTTPStatus
from http.client import NOT_FOUND
import requests
import json
import sys
from datetime import datetime
from logger import Logger

def ExecuteRequest(method, url, body={}):
    Logger.Info(f">>> [{method}] {url}: Body: {body}")    
    response = requests.request(method=method, url=url, json=body, headers={'Content-Type': 'application/json'})   
    Logger.Info(f"<<< [{method}] Respose: {HTTPStatus(response.status_code).name}:{response.status_code} -> Body:{json.dumps(response.json())}")

    return response

def TestRequest(method, url, body={}, message="", expected=[ HTTPStatus.OK ]):
    Logger.Info(f">>> {message} -> expecting HTTP {expected}" )
    response = ExecuteRequest(method, url, body)
   
    if response.status_code in expected:
        Logger.Success(f"<<< OK!\n\tAccepted values:\t{expected}\n\tReceived value:\t\tHTTP {response.status_code}")
    else:
        Logger.Error(f"<<< FAIL!\n\tAccepted values:\t{expected}\n\tReceived value:\t\tHTTP {response.status_code}")

url = "http://localhost:5000/items"

TestRequest('GET', url, {}, "Trying to get all items", [ HTTPStatus.OK, HTTPStatus.NOT_FOUND])

items = {}
qty = 10

for i in range(qty):
    id = f"item{i}"        
    items[id] = {} 
    items[id]['item'] = { f"key{i}" : f"value_{i}"  }

    TestRequest('POST', f"{url}/{id}", items[id], "Trying to insert items for first time", [ HTTPStatus.CREATED ])
    TestRequest('POST', f"{url}/{id}", items[id], "Trying to insert an item that already exists", [ HTTPStatus.OK ])
    TestRequest('GET', f"{url}/{id}", {}, f"Trying to get all item, by ID (key = {id})", [ HTTPStatus.OK ])

TestRequest('GET', f"{url}/XPTO", {}, "Trying to get a not found item (key = XPTO)", [ HTTPStatus.NOT_FOUND ])

updatedItem = {}

for k in items:
    updatedItem['item'] = { f"key{k}": f"updated_value_{k}" }
    TestRequest('PUT', f"{url}/{k}", updatedItem, f"Trying to update a item (key={k}) -> new value: {updatedItem}", [ HTTPStatus.OK ])

TestRequest('PUT', f"{url}/XPTO", updatedItem, f"Trying to update a item with non existent key (key = XPTO) new value: {updatedItem}", [ HTTPStatus.NOT_FOUND ])

for k in items:
    TestRequest('GET', f"{url}/{k}", {}, f"Trying to get an updated item (key = {k}) expecting value={updatedItem}", [ HTTPStatus.OK ])

for k in items:
    TestRequest('DELETE', f"{url}/{k}", {}, f"Trying to delete item (key = {k})", [ HTTPStatus.OK ])
    TestRequest('DELETE', f"{url}/{k}", {}, f"Trying to delete item AGAIN (key = {k})", [ HTTPStatus.NOT_FOUND ])
    TestRequest('GET', f"{url}/{k}", {}, f"Trying to get item, by ID (key = {k})", [ HTTPStatus.NOT_FOUND ])