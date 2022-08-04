#!/bin/bash
export FLASK_APP=app/$1/main && flask run --reload
