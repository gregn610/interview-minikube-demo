#!/usr/bin/env bash

# Notes
# Changed hash bang to env for robustness & portability
# Add bulletproof bash `set`s for robustness

set -e
set -u
set -o pipefail

set -x

app="demo.backend"
docker build -t ${app} .
docker run -d -p 58081:80 --name=${app} -v $PWD:/app ${app}
