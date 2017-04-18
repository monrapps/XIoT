#!/bin/sh

cd xia-core/bin
./xianet -r start

tail -f /var/log/dmesg

