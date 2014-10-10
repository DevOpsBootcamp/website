#! /bin/bash

# Update repo
git checkout master
git pull -q --ff-only

# Enable venv
if [ ! -d venv ]; then
    virtualenv venv
fi
source venv/bin/activate

# Update packages
pip install -r requirements.txt

# Nuke the old build dir
rm -rf build/

# Build slides 
make slides

# Delete non-slide content
cd build/slides
for i in $(ls daycamp*); do mv $i 99-$i; done
rm -f [a-zA-Z]*

# Disable venv
deactivate

