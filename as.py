#!/usr/bin/python3

import sys
import re
import ipaddress

# Define bits/prefix dictionary
bitprefix_dict = { "32":0, "31":1, "30":2, "29":3, "28":4, "27":5, "26":6, "25":7 }

if len(sys.argv) != 2:
	print('\nUsage: ./as.py FILE\n')
	print('Example: ./as.py networks.txt\n')
	exit('Exiting...')

userprefix = input('\nEnter desidered prefix (eg. 29): ')

try:
	val = int(userprefix)
except ValueError:
   	exit('\n[X] Invalid user input!\nExiting...\n')

if int(userprefix) > 32 or int(userprefix) < 25:
	exit('\n[X] Unsupported prefix!\n')

file = open(sys.argv[1],'r')

# Convert prefix in bit for later use with ipaddress module
prefix = bitprefix_dict.get(userprefix)
#print(prefix)

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

print('\n[*] Generating /' +str(userprefix) + ' subnets...\n')
for addr in netset:
	print(list(ipaddress.ip_network(addr).subnets(prefixlen_diff=prefix)))
