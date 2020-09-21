#!/bin/bash

# Install, provide as first agument, the directory where packages are listed

sudo apt install python3 # Just make sure we have python3
sudo apt install software-properties-common # Need that add-apt-repository
python3 ./apt-installer.py $(cwd)/$1