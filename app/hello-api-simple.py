#!/bin/python3

from flask import Flask, jsonify
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
    return { "hello" : "you" }
