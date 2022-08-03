#!/bin/bash
EXPORT_
export FLASK_APP=app/$1 && flask run --reload
