#!/bin/python3

#
# https://www.rfc-editor.org/rfc/rfc7231#section-6.1
#

from http import HTTPStatus
from flask import Flask, jsonify, Response, request
from datetime import datetime
from flasgger import Swagger, swag_from
import json

app = Flask(__name__)
app.run(debug=True, use_debugger=True, use_reloader=True)
swagger = Swagger(app)

items = {}

@app.route("/items", methods = ['GET'])
@swag_from("swagger/get_items.yml")
def get_all():
	if len(items) == 0:
		return {}, HTTPStatus.NOT_FOUND

	return { 
		'result' : items,
	}, HTTPStatus.OK


@app.route("/items/<id>", methods = ['GET'])
@swag_from("swagger/get_item.yml")
def get_from_id(id):
	if id in items:
		return { 
			"item" : items[id],
		}, HTTPStatus.OK
	
	return {}, HTTPStatus.NOT_FOUND

@app.route("/items/<id>", methods = ['POST'])
@swag_from("swagger/post_item.yml")
def post_from_id(id):
	if 'item' not in request.json:
		return {}, HTTPStatus.UNPROCESSABLE_ENTITY

	ret =  HTTPStatus.CREATED	
	if id in items:
		# item already exists, will be updated
		ret = HTTPStatus.OK

	items[id] = request.json['item']
	return {}, ret

@app.route("/items/<id>", methods = ['PUT'])
@swag_from("swagger/put_item.yml")
def put_from_id(id):
	if 'item' not in request.json:
		return {}, HTTPStatus.UNPROCESSABLE_ENTITY

	if id in items:		
		items[id] = request.json['item']
		return {}, HTTPStatus.OK

	return {}, HTTPStatus.NOT_FOUND	


@app.route("/items/<id>", methods = ['DELETE'])
@swag_from("swagger/delete_item.yml")
def delete_from_id(id):
	if id in items:
		del items[id]
		return {}, HTTPStatus.NO_CONTENT

	return {}, HTTPStatus.NOT_FOUND