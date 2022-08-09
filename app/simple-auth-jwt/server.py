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
#   https://www.devmedia.com.br/como-o-jwt-funciona/40265#:~:text=JWT%20(JSON%20Web%20Token)%20%C3%A9,permitem%20a%20autentica%C3%A7%C3%A3o%20da%20requisi%C3%A7%C3%A3o.
#

app = Flask(__name__)
swagger = Swagger(app)

# fake structfor users - simulates a database
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

# local settings
login_key = "My secret login key"
toker_key = "My very secret token key"
time_to_expire = 10

# helpers methods
def create_jwt(payload = {}):
  return jwt.encode(payload, toker_key, algorithm="HS256")

def get_userinfo(token):
  return jwt.decode(token, login_key, algorithms=[ "HS256" ])  

def create_body(pars = {}):
  pars['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  return pars

def get_claims(token):
  return jwt.decode(token, toker_key, algorithms=[ "HS256" ])  

# routes
@app.route("/login", methods = ['POST'])
@swag_from("swagger/post_login.yml")
def post_login():
  userInfo = get_userinfo(request.headers['requestToken'])

  user = userInfo['user']    
  passwd = userInfo['pass']

  if user in users:    
    if users[user]['pass'] == passwd:
      exp = datetime.now(tz=timezone.utc) + timedelta(seconds=time_to_expire)
      payload = users[user]['claims']
      payload['sub'] = user
      payload['iat'] = datetime.now(tz=timezone.utc)
      payload['exp'] = exp
      payload['iss'] = 'simple-auto-jwt-server'

      jwt = create_jwt(payload)
    
      return create_body({ 'jwt' : jwt, 'exp': exp.timestamp() }), HTTPStatus.OK

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