#!/bin/bash
pip3 install -r requirements.txt
export FLASK_APP=app/$1 && flask run --reload
