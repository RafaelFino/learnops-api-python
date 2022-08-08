#!/bin/python3

from http import HTTPStatus
from flask import Flask, jsonify, Response, request
from datetime import datetime, timedelta, timezone
import time
from flasgger import Swagger, swag_from
from ulid import ULID
import jwt

#
# Great text to read JWT: 
#   https://auth0.com/blog/how-to-handle-jwt-in-python/
#   https://pyjwt.readthedocs.io/en/latest/usage.html
#

app = Flask(__name__)
swagger = Swagger(app)

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

key = "Minha Chave"

def create_jwt(payload = {}):  
  return jwt.encode(payload, key, algorithm="HS256")

def get_claims(token):
  return jwt.decode(token, key, algorithms=[ "HS256" ])

def create_body(pars = {}):
  pars['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  return pars

@app.route("/login", methods = ['POST'])
@swag_from("swagger/post_login.yml")
def post_login():
    user = request.headers['user']
    passwd = request.headers['pass']

    if user in users:
      if users[user]['pass'] == passwd:
        payload = users[user]['claims']
        payload['iat'] = time.mktime(datetime.now(tz=timezone.utc).timetuple())
        payload['exp'] = time.mktime((datetime.now(tz=timezone.utc) + timedelta(seconds=30)).timetuple())

        jwt = create_jwt(payload)
      
        return create_body({ 'jwt' : jwt }), HTTPStatus.OK

    return create_body(), HTTPStatus.UNAUTHORIZED


@app.route("/admin", methods = ['GET'])
@swag_from("swagger/get_admin.yml")
def get_admin():
  try:
    token = request.headers['Authorization'].replace('Bearer ', '')
    claims = get_claims(token)

    print(f"Hello {claims['nick']}")

    if claims['admin'] != True:
      return create_body({ 'message': 'user do not have this permission' }), HTTPStatus.UNAUTHORIZED    
    
    print('Get admin stuff...')
    return create_body({ 'message': 'admin get are allowed' }), HTTPStatus.OK

  except Exception as e:
    return create_body({ 'message': str(e) }), HTTPStatus.UNAUTHORIZED
  
@app.route("/query", methods = ['GET'])
@swag_from("swagger/get_query.yml")
def get_query():
  try:
    token = request.headers['Authorization'].replace('Bearer ', '')
    claims = get_claims(token)

    print(f"Hello {claims['nick']}")

    if claims['query'] != True:
      return create_body({ 'message': 'user do not have this permission' }), HTTPStatus.UNAUTHORIZED    
    
    print('Get query stuff...')
    return create_body({ 'message': 'query get are allowed' }), HTTPStatus.OK

  except Exception as e:
    return create_body({ 'message': str(e) }), HTTPStatus.UNAUTHORIZED
  



