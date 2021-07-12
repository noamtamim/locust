#!/usr/bin/env bash

set -exu

echo "$@"

curl https://api.ipify.org/

curl "$1" -o locustfile.py

locust --master
