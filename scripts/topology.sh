#!/bin/sh

if [ $# -eq 0 ] ; then
   echo
   echo "No arguments supplied"
   echo "Usage: ./topology.sh monra/xia-server monra/xia-gateway-router 1 monra/xia-client-router 1 monra/xia-gateway 2 monra/xia-client 3 10 8 100 150"
   echo
   exit
fi


echo
echo

echo "Server Image: $1"
echo
echo "Gateway Routers Image: $2"
echo "Gateway Routers: $3"
echo
echo "Client Routers Image: $4"
echo "Client Routers: $5"
echo
echo "Gateways Image: $6"
echo "Gateways per Gateway-Router: $7"
echo
echo "Clients Image: $8"
echo "Clients per Client-Router: $9"
echo
echo "Motes per Gateway: $10"
echo "Data Size: $11 bytes"
echo "Requests: $12"
echo "Timeout: $13 ms" 

echo
echo


#sudo docker network create -d Server_Network
#sudo docker run -d --net=Server_Network --name Server $2  
echo "Server initialized"   

for i in $(seq 1 $3)
do
   #sudo docker network create -d Gateway_Network_$i
   #sudo docker run -d --net=Gateway_Network_$i --name Gateway_Router_$i $2   
   echo "Gateway Router $i initialized"   
   for j in $(seq 1 $7)
   do      
      z="$(( $7 * ( $i - 1 ) + $j ))"
      #sudo docker run -d --net=Gateway_Network_$i --name Gateway_$i $6
      echo "Gateway $z initialized"
      done
done

echo
echo

for i in $(seq 1 $5)
do
   #sudo docker network create -d Client_Network_$i
   #sudo docker run -d --net=Client_Network_$i --name Client_Router_$i $4
   echo "Clients Router $i initialized"
   for j in $(seq 1 $9)
   do
      z="$(( $9 * ( $i - 1 ) + $j ))"
      #sudo docker run -d --net=Client_Network_$i --name Client_$z $8     
      echo "Client $z initialized"
   done
done

echo
echo

