#!/bin/sh

sudo apt-get -y install binutils-msp430 gcc-msp430 msp430mcu gcc-avr avr-libc msp430-libc ant openjdk-8-jdk

git clone

cd contiki

git submodule update --init # necessario para cooja

