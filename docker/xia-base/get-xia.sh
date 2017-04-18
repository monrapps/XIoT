#!/bin/sh

# get XIA source 
cd /
git clone https://github.com/XIA-Project/xia-core.git
chmod -R 777 xia-core
cd xia-core
git checkout develop

# Delete xsockconf.ini files that are not for GENI XIA-prototype
#find . -name "xsockconf*.ini" -exec rm -rf {} \;

