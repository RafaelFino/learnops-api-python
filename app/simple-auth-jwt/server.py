#!/bin/python3
from http import HTTPStatus
from flask import Flask, request
from datetime import datetime, timedelta, timezone
from flasgger import Swagger, swag_from
from cripto import CriptoServer
from cryptography.hazmat.primitives import serialization
import jwt
import json

#
# References about JWT:
#	 https://auth0.com/blog/how-to-handle-jwt-in-python/
#	 https://pyjwt.readthedocs.io/en/latest/usage.html
#	 https://www.devmedia.com.br/como-o-jwt-funciona/40265#:~:text=JWT%20(JSON%20Web%20Token)%20%C3%A9,permitem%20a%20autentica%C3%A7%C3%A3o%20da%20requisi%C3%A7%C3%A3o.
#	 https://imasters.com.br/desenvolvimento/json-web-token-conhecendo-o-jwt-na-teoria-e-na-pratica
#

app = Flask(__name__)
swagger = Swagger(app)

# fake structfor users - simulates a database
users = { 
	'usuario1': {
		'pass' : 'senha1',
		'claims': {
			'routes' : [
				"query", "admin"
			],
			'nick': 'Fulano'
		}
	}, 
	'usuario2': {
		'pass' : 'senha2',
		'claims': {
			'routes' : [
				"query"
			],
			'nick': 'Beltrano'		 
		}
	}
}

# local settings
time_to_expire = 10

cripto = CriptoServer()

# helpers methods
def create_jwt(payload = {}):
	return jwt.encode(payload, key=cripto.GetPrivateKey(), algorithm='RS256')

def get_userinfo(token):
	j = cripto.Decript(token)
	return json.loads(j)

def create_headers(headers = {}):
	headers['Timestamp'] = datetime.now(tz=timezone.utc).timestamp()
	headers['Content-Type'] = 'application/json'

	return headers
	
def create_body(body = {}, message = ""):
	if len(message) > 0:
		body['message'] = message 

	return body

def get_claims(token):
	return jwt.decode(token, key=cripto.GetPublicKey(), algorithms=[ 'RS256', ], options={"verify_signature": True, "verify_exp": True})	

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
	 
			return create_body({ 'jwt' : jwt, 'exp': exp.timestamp() }), HTTPStatus.OK, create_headers()

	return create_body({}), HTTPStatus.UNAUTHORIZED, create_headers()

@app.route("/admin", methods = ['GET'])
@swag_from("swagger/get_admin.yml")
def get_admin():
	try:
		token = request.headers['Authorization'].replace('Bearer ', '')
		claims = get_claims(token)
		

		if 'admin' in claims['routes']:
			return create_body({}, f"Hello {claims['nick']}, you are allowed to request ADMIN route") , HTTPStatus.OK, create_headers()	
		
		return create_body({}, 'user do not have permission for this role') , HTTPStatus.UNAUTHORIZED, create_headers()		
	except Exception as e:
		return create_body({}, str(e)) , HTTPStatus.UNAUTHORIZED, create_headers()
	
@app.route("/query", methods = ['GET'])
@swag_from("swagger/get_query.yml")
def get_query():
	try:
		token = request.headers['Authorization'].replace('Bearer ', '')
		claims = get_claims(token)

		if 'query' in claims['routes']:
			return create_body({}, f"Hello {claims['nick']}, you are allowed to request QUERY route") , HTTPStatus.OK, create_headers()
			
		return create_body({}, 'user do not have permission for this role') , HTTPStatus.UNAUTHORIZED, create_headers()				
	except Exception as e:
		return create_body({}, str(e)) , HTTPStatus.UNAUTHORIZED, create_headers()
