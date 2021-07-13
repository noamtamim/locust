#!/usr/bin/env bash

set -exu

echo "$@"

URL="$1"
MASTER_HOST="$2"
MASTER_PORT="$3"

curl "$URL" -o locustfile.py

# just for connectivity testing
curl http://$MASTER_HOST:8089

locust --worker --master-host=$MASTER_HOST --master-port=$MASTER_PORT
