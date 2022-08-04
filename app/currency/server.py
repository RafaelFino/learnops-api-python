#!/bin/python3

from crypt import methods
from http import HTTPStatus
from flask import Flask, jsonify, Response, request
from datetime import datetime
from flasgger import Swagger, swag_from
from currencies import CurrenciesService
import json

app = Flask(__name__)
swagger = Swagger(app)

service = CurrenciesService()

# calc elapsedtime in method
def getElapsedTime(start:datetime):
  return f"{(datetime.now() - start).total_seconds()*1000:.3f}ms"

# creates a dict struct to body response
def createResponseBody(ret={}):
  ret['lastUpdate'] = service.LastUpdate.strftime("%m-%d-%Y %H:%M:%S")
  ret['timestamp'] = datetime.now().strftime("%m-%d-%Y %H:%M:%S")  

  return ret

#API methods
@app.route("/all", methods = ['GET'])
@swag_from("swagger/get_all.yml")
def get_all(): 
  start = datetime.now()
  ret = createResponseBody(service.Get())

  ret['elapsedTime'] = getElapsedTime(start)
  return json.dumps(ret, indent=4), HTTPStatus.OK

@app.route("/<code>", methods = ['GET'])
@swag_from("swagger/get_code.yml")
def get_code(code): 
  start = datetime.now()
  ret = createResponseBody({ code: service.GetByCode(code)})

  returnCode = HTTPStatus.OK

  if ret[code] == None:
    returnCode = HTTPStatus.NOT_FOUND
  
  ret['elapsedTime'] = getElapsedTime(start)
  return json.dumps(ret, indent=4), returnCode

@app.route("/convert", methods = ['POST'])
@swag_from("swagger/post_convert.yml")
def post_convert():
  start = datetime.now()
  ret = createResponseBody()
  
  body = request.json

  # Check body struct
  if 'value' not in body:
    return json.dumps(ret, indent=4), HTTPStatus.BAD_REQUEST
  
  value = float(body['value'])
    
  # use USD as a default value
  if 'codes' not in body:
    codes = [ "USD" ]
  else:
    if len(body['codes']) == 0:
      codes = [ "USD" ]
    else:
      codes = body['codes']

  ret['result'] = {}
  for code in codes:
    curr = service.GetByCode(code)

    if curr == None:    
      if 'notFound' not in ret:
        ret['notFound'] = []

      ret['notFound'].append(code)
    else:      
      ret['result'][code.upper()] = curr['ask'] * value     
  

  if 'notFound' in ret:
    return json.dumps(ret, indent=4), HTTPStatus.NOT_FOUND
  
  ret['elapsedTime'] = getElapsedTime(start)
  return json.dumps(ret, indent=4), HTTPStatus.OK