#!/bin/sh

git clone https://github.com/contiki-os/contiki.git \
cd contiki \
git submodule update --init \
export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8

