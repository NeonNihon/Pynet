#!/usr/bin/env python

from __future__ import print_function
from telnetlib import Telnet

ip_addr = '184.105.247.70'
username = 'pyclass'
password = '88newclass'


t = Telnet(ip_addr)
t.read_until('sername: ')
t.write(username + '\n')
t.read_until('assword: ')
t.write(password + '\n')
t.read_until('#')
t.write('show ip interface brief\n')
print(t.read_until('#'))
