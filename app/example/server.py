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
    content:
      application/json:
    responses:
      200:
        description: Success
        content:
          application/json:
            schema:
              type: object
              properties:
                - hello:
                  type: string           
    """
    return { "hello" : "you" }
