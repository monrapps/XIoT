#! /usr/bin/env python
import sys

ipv6_list = []

def getipv6():
	text = open('index.html').readlines()
	for x in text:
		if x[:6] == "aaaa::":
			count = -1
			for y in x:
				count = count + 1
				if y == "/":
					ipv6_list.append(x[:count])					
		elif x[17:23]  == "aaaa::":
			for y in range(2, len(x)):
				if x[y] == "/":
					ipv6_list.append(x[17:y])

getipv6()
print ipv6_list[0]

ip = 0

print str(ip+1)+"."+sys.argv[1]+"."+sys.argv[2]
