#!/bin/bash
sudo yum install protobuf-devel protobuf-compiler openssl openssl-devel tkinter python-devel python-requests swig make gcc-c++ doxygen python-sphinx git
	
if [ ! -d "xia-core" ]; then
	git clone https://github.com/XIA-Project/xia-core.git
else
	cd xia-core
	git pull
	make clean
	cd ..	
fi	
cd xia-core
./configure
make

