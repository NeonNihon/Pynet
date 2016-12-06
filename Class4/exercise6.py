#!/usr/bin/env python
from __future__ import print_function
from netmiko import ConnectHandler


def show_arp(conn):
    arp = conn.send_command('show arp')
    return arp


def print_output(conn):
    print(str(conn.host).center(20, '*'))
    print(show_arp(conn))
    print('END'.center(20, '*'))


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

juniper_srx = {
    'device_type': 'juniper',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': '88newclass',
    'port': 22
}

rtr1 = ConnectHandler(**pynet1)
rtr2 = ConnectHandler(**pynet2)
srx1 = ConnectHandler(**juniper_srx)

print_output(rtr1)
print_output(rtr2)
print_output(srx1)


rtr1.disconnect()
rtr2.disconnect()
srx1.disconnect()
