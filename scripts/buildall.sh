#!/bin/bash

cd ../docker

cd xia-base

docker build -t xia-base .

cd ..

cd xia-server

docker build -t xia-server .

cd ..

cd xia-router

docker build -t xia-router .

cd ..

cd xia-gateway

docker build -t xia-gateway .

cd ..

cd xia-client

docker build -t xia-client .

cd ..

