#!/bin/bash
export FLASK_APP=app/$1/server && flask run --reload --host=0.0.0.0
