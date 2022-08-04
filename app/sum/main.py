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
    numbers = request.json['numbers']
    result = 0

    for i in numbers:
      result += i    

    return { 
      "result" : result,
      "timestamp:" : datetime.now()
    }, HTTPStatus.OK
