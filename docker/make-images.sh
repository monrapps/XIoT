#!/bin/sh

cd xia-base

sudo docker build -t xia-base:latest .

cd ..

cd xia-client

sudo docker build -t xia-client:latest .

cd ..

cd xia-gateway

sudo docker build -t xia-gateway:latest .

cd ..

cd xia-router

sudo docker build -t xia-router:latest .

cd ..

cd xia-server

sudo docker build -t xia-server:latest .

cd ..

cd ipv6-base

sudo docker build -t ipv6-base:latest .

cd ..

cd ipv6-client

sudo docker build -t ipv6-client:latest .

cd ..

cd ipv6-gateway

sudo docker build -t ipv6-gateway:latest .

cd ..

cd ipv6-router

sudo docker build -t ipv6-router:latest .

cd ..

cd ipv6-server

sudo docker build -t ipv6-server:latest .

cd ..
