#!/usr/bin/env bash

pip install -r requirements-dev.txt
if [[ $TRAVIS_PYTHON_VERSION == 2.6 ]]; then pip install -r requirements26-dev.txt; fi
if [[ $TRAVIS_PYTHON_VERSION == 2.7 ]]; then pip install -r requirements27-dev.txt; fi
if [[ $TRAVIS_PYTHON_VERSION == 3.4 ]]; then pip install -r requirements34-dev.txt; fi
if [[ $TRAVIS_PYTHON_VERSION == 3.5 ]]; then pip install -r requirements35-dev.txt; fi