#!/bin/python3

from http import HTTPStatus
from flask import Flask, request
from datetime import datetime, timedelta
from flasgger import Swagger, swag_from
from ulid import ULID
from users import UserStorage

app = Flask(__name__)
swagger = Swagger(app)

header = { 'Content-Type': 'application/json' }
tokens = {}
timeToExpire = 1

def create_body(pars = {}):
  pars['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  return pars

@app.route("/login", methods = ['POST'])
@swag_from("swagger/post_login.yml")
def post_login():
    user = request.headers['user']
    passwd = request.headers['pass']

    if user in UserStorage.Users:
      if UserStorage.Users[user] == passwd:
        token = str(ULID.from_datetime(datetime.now()))
        tokens[token] = datetime.now()
        
        return create_body({ 'token' : token }), HTTPStatus.OK, header

    return create_body(), HTTPStatus.UNAUTHORIZED, header

@app.route("/validate", methods = ['POST'])
@swag_from("swagger/post_validate.yml")
def post_validate():
  token = request.headers['token']
  if token in tokens:
    if datetime.now() - tokens[token] <= timedelta(minutes=timeToExpire):
      return create_body(), HTTPStatus.OK, header
    else:
      return create_body({ 'message' : 'expired' }), HTTPStatus.UNAUTHORIZED, header

  return create_body(), HTTPStatus.UNAUTHORIZED, header


