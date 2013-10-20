#!/bin/bash

# Put slides from ./source/slides into ./slides, and make 'em pretty

sphinx-build -b slides ./source/slides/ ./build/html/slides

echo "slides made!"
