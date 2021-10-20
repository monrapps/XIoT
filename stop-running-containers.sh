#!/bin/sh

# usage 
# sudo sh stop-running-containers c C g G 
# c = number of Clients per Client Routers
# C = number of Client Routers
# g = number of Gateways per Gateway Router
# G - number of Gateway Routers

A=`expr $1 \* $2`

for i in $(seq 1 $A)
do 
echo "Stopping client: $i" 

docker stop Client_$i

done

for j in $(seq 1 $2)
do 
echo "Stopping client router: $j" 

docker stop Clients_Router_$j

done

B=`expr $3 \* $4`


for l in $(seq 1 $B)
do 
echo "Stopping gateway: $l" 

docker stop Gateway_$l

done

for m in $(seq 1 $4)
do 
echo "Stopping gateway router: $m" 

docker stop Gateways_Router_$m

done

docker stop Server

docker container prune -f
