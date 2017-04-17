#!/bin/sh

apt-get -y install ant openjdk-8-jdk

git clone https://github.com/contiki-os/contiki.git 
cd contiki 
git submodule update --init 

