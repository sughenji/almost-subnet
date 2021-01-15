#!/usr/bin/python3

import sys
import re
import ipaddress

if len(sys.argv) != 2:
	print('\nUsage: ./as.py FILE\n')
	exit('Exiting...')
file = open(sys.argv[1],'r')

for line in file.readlines():
	line = line.strip('\n')
	try:
		ipaddress.ip_address(line)
		print('IP ' + str(line) + ' is a valid IPv4 address')
		print('IP ' + str(line) + ' is in subnet: ' + str(ipaddress.ip_network('192.168.0.8/30')))
	except ValueError:
		print('IP ' + str(line) + ' is NOT a valid address')

#x = [ "192.168.0.1", "192.168.0.2", "192.168.0.3", "192.168.0.4" ]
#y = [ "192.168.0.1", "192.168.0.5" ]

#result = re.findall([y], [x])
#result = x + y
#print(result)

list(ipaddress.ip_network('192.168.0.0/29').hosts())
print(list)
