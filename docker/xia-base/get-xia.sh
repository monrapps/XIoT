#!/bin/sh

# get XIA source 

git clone https://github.com/XIA-Project/xia-core.git
cd xia-core
git checkout develop
cd ..
chmod -R 777 xia-core

# Delete xsockconf.ini files that are not for GENI XIA-prototype
#find . -name "xsockconf*.ini" -exec rm -rf {} \;

