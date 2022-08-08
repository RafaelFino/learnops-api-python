#!/bin/python3

from crypt import methods
from http import HTTPStatus
from flask import Flask, jsonify, Response, request
from datetime import datetime, timedelta
from flasgger import Swagger, swag_from
from ulid import ULID

app = Flask(__name__)
swagger = Swagger(app)

users = { 'usuario1': 'senha1', 'usuario2': 'senha2' }
tokens = {}
timeToExpire = 1

@app.route("/login", methods = ['POST'])
@swag_from("swagger/post_login.yml")
def post_login():
    user = request.headers['user']
    passwd = request.headers['pass']

    if user in users:
      if users[user] == passwd:
        token = str(ULID.from_datetime(datetime.now()))
        tokens[token] = datetime.now()
        
        return {
          'token' : token,
          'timestamp:' : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }, HTTPStatus.OK        

    return { 
      'timestamp:' : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }, HTTPStatus.UNAUTHORIZED

@app.route("/validate", methods = ['POST'])
@swag_from("swagger/post_validate.yml")
def post_validate():
  token = request.headers['token']
  if token in tokens:
    if datetime.now() - tokens[token] <= timedelta(minutes=timeToExpire):
      return {
        'timestamp:' : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      }, HTTPStatus.OK
    
    else:
      return {
        'message' : 'expired',
        'timestamp:' : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      }, HTTPStatus.UNAUTHORIZED

  return {
    'timestamp:' : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  }, HTTPStatus.UNAUTHORIZED


