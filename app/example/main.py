#!/bin/python3

from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route("/")
def awnser():
    """
    Just answer request
    ---
    responses:
      200:
        description: Success
    """
    return { "hello" : "you" }
