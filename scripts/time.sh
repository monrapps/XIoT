#!/bin/sh

while getopts C:CR:G:GR:M:RQ:T:S option
do
    case "${option}"
    in
        C) CLIENTS=${OPTARG};;
        CR) CLIENTROUTERS=${OPTARG};;
        G) GATEWAYS=${OPTARG};;
        GR) GATEWAYROUTERS=${OPTARG};;
        M) MOTES=${OPTARG};;
    esac
done

docker run -d xia-server

sleep 5

for i in `seq 1 $GATEWAYS`;
do
    docker run -d xia-gateway &
done

sleep 5

for i in `seq 1 $CLIENTS`;
do
    docker run xia-client &
done



