#!/usr/bin/env bash

set -exu

curl "$1" -o locustfile.py

locust --master
