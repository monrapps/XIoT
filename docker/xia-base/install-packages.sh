#!/bin/sh

# keep grub UI from coming up
#apt-mark hold grub

# make sure os is up to date
apt-get update
apt-get -y upgrade

# Install required packages
apt-get install -y git g++ make openssl libssl-dev
apt-get install -y libprotobuf-dev protobuf-compiler
apt-get install -y python-tk python-dev python-setuptools python-crypto python-requests
apt-get install -y swig
apt-get install -y python-argparse
apt-get install -y python-pygame
apt-get install -y libffi-dev python-crypto python-protobuf python-networkx python-pip

# tools
#apt-get install -y vim tmux ack-grep curl socat netcat wget stunnel
apt-get install -y net-tools

#pip install --upgrade pip
#pip install pynacl

