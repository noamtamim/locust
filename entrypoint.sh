#!/usr/bin/env bash

<< ////

Usage:

Pass the URL of the locustfile.py file as the first argument. All other arguments go directly to locust.
DO NOT pass a `-f` argument!

////

set -exu

function download() {
    # avoid installing curl
    python -c "import urllib.request as req; req.urlretrieve('$1', '$2')"
}

download "$1" locustfile.py

shift

locust $*

