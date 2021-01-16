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

print('\n[*] Checking your file...')
for line in file.readlines():
	line = line.strip('\n')
	try:
		ipaddress.ip_address(line)
		#print('IP ' + str(line) + ' is a valid IPv4 address')
		listips.append(ipaddress.ip_address(line))
	except ValueError:
		print('\n[X] Error! Line with "' + str(line) + '" does NOT contain a valid IPv4 address.')
		exit('\n[X] Please sanitize your file first.')
print('\n[*] File is OK!')

print('\n[*] Sorting file...')
listips.sort()

print(listips)


