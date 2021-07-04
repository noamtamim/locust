#!/usr/bin/env bash

<< ////

Usage:

Pass the URL (http/https/s3) of the locustfile.py file as the first argument. All other arguments go directly to locust.
DO NOT pass a `-f` argument!

////

set -exu

function download() {
    if [[ $1 == s3:* ]]; then
      aws s3 cp "$1" "$2"
    else
      curl "$1" -o "$2"
    fi
}

download "$1" locustfile.py

locust $*

