#!/bin/python3

from crypt import methods
from http import HTTPStatus
from flask import Flask, jsonify, Response, request
from datetime import datetime
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/", methods = ['POST'])
@swag_from("body-swagger.yml")
def get_name_from_json_body():
    name = request.json['name']
    if len(name) == 0:
      name = "envergonhado"

    return { 
      "hello-from-json-body" : name,
      "timestamp:" : datetime.now()
    }, HTTPStatus.OK
