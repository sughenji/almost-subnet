#!/usr/bin/python3

import sys
import ipaddress

if len(sys.argv) != 2:
	print('\nUsage: ./as.py FILE\n')
	print('FILE must contain IP addresses already assigned to your customers (one per line).\n')
	exit('Exiting...')

prefix = input('\nEnter desired prefix (eg. 29): ')

try:
	val = int(prefix)
except ValueError:
   	exit('\n[X] Invalid user input!\nExiting...\n')

if int(prefix) not in range(25,31):
	exit('\n[X] Unsupported prefix!\n')

file = open(sys.argv[1],'r')

# Initialize empty lists
listips = [] 
almostsubnets = []

print('\n...checking your file...')
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

file = open(sys.argv[1],'r')

# Populating set with relevant networks, according to provided list
for item in listips:
	IP = ipaddress.ip_interface(str(item) + '/' + str(prefix))
	NET = IP.network
	netset.add(NET)

netset = sorted(netset)

# Finding "interesting" subnets
print('\n...harvesting "almost subnets", please wait...\n')
for net in netset:
	count = 0
	for item in listips:
		if ipaddress.ip_interface(item) in ipaddress.IPv4Network(net):
			#print('Considering ip: ' + str(ipaddress.ip_interface(item)) + ' in subnet: ' + str(ipaddress.IPv4Network(net)) + '\n')
			count += 1
	if count == 1:
		print('...this network is almost free: ' + str(net) + '!\n')
		almostsubnets.append(net)

# Check if there is at least something...
if not almostsubnets:
	print('[X] Sorry, nothing found.')
	exit()
else:
	print('...Finding "interesting" IP addresses...\n')
	for netitem in almostsubnets:
		for item in listips:
			if ipaddress.ip_interface(item) in ipaddress.IPv4Network(netitem):
				print('[*] You can recover subnet: ' + str(netitem) + ' by just deassigning IP: ' + str(item) + '!\n')
