#!/bin/python3

from http import HTTPStatus
from flask import Flask, jsonify, Response, request
from datetime import datetime, timedelta, timezone
import time
from flasgger import Swagger, swag_from
import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

#
# Great text to read JWT: 
#   https://auth0.com/blog/how-to-handle-jwt-in-python/
#   https://pyjwt.readthedocs.io/en/latest/usage.html
#

app = Flask(__name__)
swagger = Swagger(app)

# users fake struct
users = { 
  'usuario1': {
    'pass' : 'senha1',
    'claims': {
      'admin': True,
      'query': True,
      'nick': 'Fulano'
    }
  }, 
  'usuario2': {
    'pass' : 'senha2',
    'claims': {
      'admin': False,
      'query': True,
      'nick': 'Beltrano'     
    }
  }
}

def create_jwt(payload = {}):
  with open("./keys/jwtRSA256-private.pem", "rb") as key_file:
    return jwt.encode(payload, key_file.read(), algorithm="RS256")

def get_claims(token):
  with open("./keys/jwtRSA256-public.pem", "rb") as key_file:
    data = jwt.decode(token, key_file.read(), algorithms=[ "RS256" ])
    return data

login_key = "My secret login key"

def get_userinfo(token):
  return jwt.decode(token, login_key, algorithms=[ "HS256" ])  

def create_body(pars = {}):
  pars['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  return pars          

time_to_expire = 2

@app.route("/login", methods = ['POST'])
@swag_from("swagger/post_login.yml")
def post_login():
  userInfo = get_userinfo(request.headers['requestToken'])

  user = userInfo['user']    
  passwd = userInfo['pass']

  if user in users:
    if users[user]['pass'] == passwd:
      payload = users[user]['claims']
      payload['iat'] = datetime.now(tz=timezone.utc)
      payload['exp'] = datetime.now(tz=timezone.utc) + timedelta(seconds=time_to_expire)

      jwt = create_jwt(payload)
    
      return create_body({ 'jwt' : jwt }), HTTPStatus.OK

  return create_body(), HTTPStatus.UNAUTHORIZED


@app.route("/admin", methods = ['GET'])
@swag_from("swagger/get_admin.yml")
def get_admin():
  try:
    token = request.headers['Authorization'].replace('Bearer ', '')
    claims = get_claims(token)

    if claims['admin'] != True:
      return create_body({ 'message': 'user do not have permission for this role' }), HTTPStatus.UNAUTHORIZED    
    
    return create_body({ 
      'message': f"Hello {claims['nick']}, you are allowed to request this",
    }), HTTPStatus.OK

  except Exception as e:
    return create_body({ 'message': str(e) }), HTTPStatus.UNAUTHORIZED
  
@app.route("/query", methods = ['GET'])
@swag_from("swagger/get_query.yml")
def get_query():
  try:
    token = request.headers['Authorization'].replace('Bearer ', '')
    claims = get_claims(token)

    if claims['query'] != True:
      return create_body({ 'message': 'user do not have permission for this role' }), HTTPStatus.UNAUTHORIZED    
    
    return create_body({ 
      'message': f"Hello {claims['nick']}, you are allowed to request this",
    }), HTTPStatus.OK

  except Exception as e:
    return create_body({ 'message': str(e) }), HTTPStatus.UNAUTHORIZED
  



