#!/bin/python3

from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/ping")
def ping():
    return { "timestamp:" : datetime.now()  }
