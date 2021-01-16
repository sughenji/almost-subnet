#!/usr/bin/python3

import sys
import re
import ipaddress

if len(sys.argv) != 2:
	print('\nUsage: ./as.py FILE\n')
	exit('Exiting...')
file = open(sys.argv[1],'r')

# Initialize empty list
listips = [] 
# Initialize empyt set
netset = set()

print('\n[*] Checking your file...')
for line in file.readlines():
	line = line.strip('\n')
	try:
		ipaddress.ip_address(line)
		#print('IP ' + str(line) + ' is a valid IPv4 address')
		# Insert IP in list
		listips.append(ipaddress.ip_address(line))
		# Replace last octet with 0, converting in /24 network address
		line = line[:line.rfind('.')+1] + '0/24'
		#line = line[:line.rfind('.')+1] + '0'
		# Add /24 networks to a set
		netset.add(line) 
	except ValueError:
		print('\n[X] Error! Line with "' + str(line) + '" does NOT contain a valid IPv4 address.')
		exit('\n[X] Please sanitize your file first.')
print('\n[*] File is OK!')

#print(netset)
print('\n[*] Generating /29 subnets for every network...')
for addr in ipaddress.IPv4Network(netset):
	list(ipaddress.ip_network(addr).subnet(prefixlen_diff=5))	
	

#print('\n[*] Sorting file...')
#listips.sort()


