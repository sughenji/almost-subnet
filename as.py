#!/usr/bin/python3

import re,ipaddress

#x = [ "192.168.0.1", "192.168.0.2", "192.168.0.3", "192.168.0.4" ]
#y = [ "192.168.0.1", "192.168.0.5" ]

#result = re.findall([y], [x])
#result = x + y
#print(result)

#mask = 30
#ip = 192.168.0.2

#network = ipaddress.ip_network('192.168.0.2/30')
#print(network)

#list = [0, 0, 0, 0]
#for i in range(0,4):
#	list[i] = i+1
#
#print(list)
#otherlist = [2]
#
#result = re.findall

list(ipaddress.ip_network('192.168.0.0/29').hosts())
print(list)
