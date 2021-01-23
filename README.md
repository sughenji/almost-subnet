# almost-subnet

This tool takes a list of already assigned IP addresses and try to find *almost empty subnets*, that is: with just one address taken.
You just need to deassign that IP to recover a subnet with desired prefix.

IPv4 only :-)

`$ ./as.py FILE

Enter desired prefix (eg. 29): 29

...checking your file...

[*] File is OK!

...harvesting "almost subnets", please wait...

...this network is almost free: 192.168.0.48/29!

...this network is almost free: 192.168.0.8/29!

...Finding "interesting" IP addresses...

[*] You can recover subnet: 192.168.0.48/29 by just deassigning IP: 192.168.0.55!

[*] You can recover subnet: 192.168.0.8/29 by just deassigning IP: 192.168.0.9!
`
