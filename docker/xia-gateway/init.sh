#!/bin/sh

cd xia-core/bin
./xianet -t start

#sleep 5

cd ../applications/example
./time_of_day_server

