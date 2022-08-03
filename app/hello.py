#!/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def awnser():
    return "Ola..."

@app.route("/hello/<name>")
def named_awnser(name):
    return f"Ola <b>{name}</b>!"
