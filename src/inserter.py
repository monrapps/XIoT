#! /usr/bin/env python
import os
import re
import sys
import fileinput

for line in fileinput.FileInput("ipv6-rpl-udp.csc",inplace=1):
    if "</mote>" in line:
        line=line.replace(line,line+"<mote><breakpoints /><interface_config>se.sics.cooja.interfaces.Position<x>0.0</x><y>0.0</y><z>0.0</z></interface_config><interface_config>se.sics.cooja.mspmote.interfaces.MspMoteID<id>"+moteid+"</id></interface_config><motetype_identifier>sky2</motetype_identifier></mote>\n")
    print line,
    break
