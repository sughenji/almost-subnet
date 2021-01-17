#!/usr/bin/python3

import sys,ipaddress

if len(sys.argv) != 2:
	print('\nUsage: ./as.py FILE\n')
	print('Example: ./as.py networks.txt\n')
	exit('Exiting...')

prefix = input('\nEnter desidered prefix (eg. 29): ')

try:
	val = int(prefix)
except ValueError:
   	exit('\n[X] Invalid user input!\nExiting...\n')

if int(prefix) > 32 or int(prefix) < 25:
	exit('\n[X] Unsupported prefix!\n')

file = open(sys.argv[1],'r')

# Initialize empty list
listips = [] 
subnetips = []

print('\n[*] Checking your file...')
for line in file.readlines():
	line = line.strip('\n')
	try:
		ipaddress.ip_address(line)
		# Populating IP list...	
		listips.append(line)
	except ValueError:
		print('\n[X] Error! Line with "' + str(line) + '" does NOT contain a valid IPv4 address.')
		exit('\n[X] Please sanitize your file first.')
print('\n[*] File is OK!')

# Initialize empty set ("creating an empty set is a bit tricky...")
netset = {}
netset = set()

# Populating networks list (as a set, to avoid duplicates)
for item in listips:
	IP = ipaddress.ip_interface(str(item) + '/' + str(prefix))
	NET = IP.network
	netset.add(NET)

# Populating IP addresses in every subnet	
for net in netset:
	for x in ipaddress.IPv4Network(net):
		#subnetips.append(x)
		print(x)
		
	
		

