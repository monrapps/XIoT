#!/bin/sh

gnome-terminal --tab -e "/bin/bash -c 'sudo docker logs Server -f;exec bash'" \
gnome-terminal --tab -e "/bin/bash -c 'sudo docker logs Client_1 -f;exec bash'" \
gnome-terminal --tab -e "/bin/bash -c 'sudo docker logs Gateway_1 -f;exec bash'" \
gnome-terminal --tab -e "/bin/bash -c 'sudo docker logs Clients_Router_1 -f;exec bash'" \
gnome-terminal --tab -e "/bin/bash -c 'sudo docker logs Gateways_Router_1 -f;exec bash'" 
