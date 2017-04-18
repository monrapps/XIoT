#!/bin/sh

docker run -d xia-server

sleep 5

docker run -d xia-gateway

sleep 5

docker run xia-client

