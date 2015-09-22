#!/bin/bash

# Script for building the docs repo locally for testing feature branches and
# the like.  Can be run from any directory in the docs repo.

# Run in correct dir
DIR=`dirname $0`/../
cd $DIR

# Enable venv
if [ ! -d venv ]; then
    virtualenv venv
fi
source venv/bin/activate

# Update packages
pip install -r requirements.txt

# Build docs
SPHINXOPTS="-W" make -e slides

# Disable venv
deactivate
