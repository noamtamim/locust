#!/usr/bin/env bash

set -exu

echo "$@"

URL="$1"
MASTER_HOST="$2"
MASTER_PORT="$3"

curl "$URL" -o locustfile.py

ping -c4 $MASTER_HOST

locust --worker --master-host=$MASTER_HOST --master-port=$MASTER_PORT
