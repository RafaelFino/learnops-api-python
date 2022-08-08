#!/bin/bash
ssh-keygen -t rsa -b 4096 -m PEM -f ./etc/keys/jwtRSA256-private.pem -N ''
openssl rsa -in ./etc/keys/jwtRSA256-private.pem -pubout -outform PEM -out ./etc/keys/jwtRSA256-public.pem
