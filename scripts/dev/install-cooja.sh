#!/bin/sh

cd ~

sudo apt-get -y install binutils-msp430 gcc-msp430 msp430mcu gcc-avr avr-libc msp430-libc ant openjdk-8-jdk

if [ ! -d "contiki" ]; then
	git clone https://github.com/monrapps/contiki.git
else
	cd contiki
	git pull
	cd ..	
fi

cd contiki

git submodule update --init 

