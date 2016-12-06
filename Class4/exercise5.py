#!/usr/bin/env python
from __future__ import print_function
from netmiko import ConnectHandler

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
    'port': 22
}


net_connect = ConnectHandler(**pynet2)
net_connect.config_mode()

if net_connect.check_config_mode() is True:
    print(net_connect.find_prompt())

net_connect.exit_config_mode()
net_connect.disconnect()
