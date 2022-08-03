#!/bin/python3

from http import HTTPStatus
from flask import Flask, jsonify, Response
from datetime import datetime
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/hello")
def awnser():
    """
    Anonymous hello answer
    ---
    responses:
      200:
        description: Success
    """
    return { 
      "hello" : "you",
      "timestamp:" : datetime.now() 
    }, HTTPStatus.OK
    

@app.route("/hello/<name>")
def named_awnser(name):
    """
    Named hello answer
    ---
    parameters:
      - name: name
        in: path
        type: string
        required: true
    responses:
      200:
        description: Success
    """
    if len(name) == 0:
      name = "envergonhado"

    return { 
      "hello" : name,
      "timestamp:" : datetime.now()
    }, HTTPStatus.OK
