#! /usr/bin/env python

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

getipv6()
print ipv6_list[0]

