#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )

# Install, provide as first agument, the directory where packages are listed

sudo apt install python3 # Just make sure we have python3
sudo apt install software-properties-common # Need that add-apt-repository
python3 $DIR/apt-installer.py $(abspath $1)