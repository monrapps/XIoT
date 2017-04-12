#!/bin/sh

echo "Clients per Client-Router: $1"
echo "Client-Routers: $2"
echo "Gateways per Gateway-Router: $3"
echo "Gateway-Routers: $4"
echo "Motes per Gateway: $5"
echo "Data Size: $6"
echo "Requests: $7"


for i in $(seq 1 $2)
do
   echo "Clients-Router $i initialized"
   for j in $(seq 1 $1)
   do
      echo "Client `expr $i \* $j` initialized"
   done
done

for i in $(seq 1 $4)
do
   echo "Gateway-Router $i initialized"
   for j in $(seq 1 $3)
   do
      echo "Gateway `expr $i \* $j` initialized"
   done
done
