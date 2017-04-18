#!/bin/sh

cd xia-core/bin
./xianet -r -n start

tail -f /var/log/dmesg

