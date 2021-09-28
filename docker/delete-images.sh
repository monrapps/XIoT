#!/bin/sh

sudo docker rmi xia-client
sudo docker rmi xia-server
sudo docker rmi xia-router
sudo docker rmi xia-gateway
sudo docker rmi xia-base

sudo docker rmi ipv6-client
sudo docker rmi ipv6-server
sudo docker rmi ipv6-router
sudo docker rmi ipv6-gateway
sudo docker rmi ipv6-base
