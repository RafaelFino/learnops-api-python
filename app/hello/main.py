#!/bin/python3

from http import HTTPStatus
from flask import Flask, jsonify, Response
from datetime import datetime
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)
 
@app.route("/hello/<name>")
@swag_from("swagger.yml")
def named_answer(name):
    if len(name) == 0:
      name = "envergonhado"

    return { 
      "hello" : name,
      "timestamp:" : datetime.now()
    }, HTTPStatus.OK
