#!/usr/bin/env python
from __future__ import print_function
from netmiko import ConnectHandler

pynet1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': '88newclass',
    'port': 22
}
pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
    'port': 22
}

rtr1 = ConnectHandler(**pynet1)
rtr2 = ConnectHandler(**pynet2)

rtr1.send_config_from_file(config_file='config_file.txt')
rtr2.send_config_from_file(config_file='config_file.txt')

print(rtr1.send_command('show running-config | include buffered'))
print(rtr2.send_command('show running-config | include buffered'))

rtr1.disconnect()
rtr2.disconnect()
