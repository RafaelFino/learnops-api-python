#!/bin/bash

arr=( ping example hello body sum crud currency auth auth-jwt)

if [ -z "$1" ]; then
    printf "#\n# %s" "API name are expected! Try one of available options:"
    printf '\n#\t%s' "${arr[@]}"
    printf '\n#'
    exit 1
fi

if ! [ -f app/$1/server.py ]; then    
    printf "#\n# %s" "API not found! Try one of available options:"
    printf '\n#\t%s' "${arr[@]}"
    printf '\n#'
    exit 1
fi

export FLASK_APP=app/$1/server && export FLASK_DEBUG=1 && flask run --reload --host=0.0.0.0 --debugger
