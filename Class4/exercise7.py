#!/usr/bin/env python
from __future__ import print_function
from netmiko import ConnectHandler

buffer_size = input('New buffer size <4096-2147483647>: ')
cmd = ['logging buffered {0}'.format(int(buffer_size))]
pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
    'port': 22
}

rtr2 = ConnectHandler(**pynet2)
rtr2.send_config_set(cmd)

print(rtr2.send_command('show running-config | include buffered'))

rtr2.disconnect()
