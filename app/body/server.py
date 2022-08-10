#!/bin/python3

from crypt import methods
from http import HTTPStatus
from flask import Flask, jsonify, Response, request
from datetime import datetime
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/", methods = ['POST'])
@swag_from("swagger.yml")
def post_sum():
    name = request.json['name']

    return { 
      "hello" : name,
      "timestamp:" : datetime.now()
    }, HTTPStatus.OK
