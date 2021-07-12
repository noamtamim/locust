#!/usr/bin/env bash

<< ////

Usage:

Pass the URL of the locustfile.py file as the first argument. All other arguments go directly to locust.
DO NOT pass a '-f' argument!

////

set -exu


echo My IP: $(curl https://api.ipify.org/)

curl "$1" -o locustfile.py

shift

locust $*

