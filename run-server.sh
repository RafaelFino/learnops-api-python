#!/bin/bash

arr=( ping example hello body sum crud currency auth auth-jwt)

if [ -z "$1" ]; then
    printf "#\n# %s" "API name are expected! Try one of available options:"
    printf '\n#\t%s' "${arr[@]}"
    printf '\n#'
fi

if [[ "${arr[*]}" =~ "${1}" ]]; then
    export FLASK_APP=app/$1/server && export FLASK_DEBUG=1 && flask run --reload --host=0.0.0.0 --debugger
else
    printf "#\n# %s" "API $1 not found! Try one of available options:"
    printf '\n#\t%s' "${arr[@]}"
    printf '\n#'
fi
