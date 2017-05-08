#!/usr/bin/env bash

set -e -x

pushd cp1_amity
    echo "Install Project Requirements"
    pip install -r requirements.txt

    echo "Run The Tests"
    nosetests -v
popd