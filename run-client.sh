#!/bin/bash

arr=( ping example hello body sum crud currency auth auth-jwt)

if [ -z "$1" ]; then
    printf "#\n# %s" "API name are expected! Try one of available options:"
    printf '\n#\t%s' "${arr[@]}"
    printf '\n#'
    exit 1
fi

if ! [ -f app/$1/client.py ]; then    
    printf "#\n# %s" "API not found! Try one of available options:"
    printf '\n#\t%s' "${arr[@]}"
    printf '\n#'
    exit 1
fi

python3 app/$1/client.py