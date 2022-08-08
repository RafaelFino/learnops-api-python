#!/bin/bash
mkdir ./keys
ssh-keygen -t rsa -b 1024 -m PEM -f ./keys/jwtRSA256-private.pem -N ''
openssl rsa -in ./keys/jwtRSA256-private.pem -pubout -outform PEM -out ./keys/jwtRSA256-public.pem
