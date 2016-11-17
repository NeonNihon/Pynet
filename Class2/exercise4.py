#!/usr/bin/env python

from __future__ import print_function
import snmp_helper

host_list = ['184.105.247.71', '184.105.247.71']
oid_name = '.1.3.6.1.2.1.1.5.0'
oid_description = '.1.3.6.1.2.1.1.1.0'
community = 'galileo'

for host in host_list:
    host_name = snmp_helper.snmp_extract(snmp_helper.snmp_get_oid((
        host, community, 161), oid_name))
    host_description = snmp_helper.snmp_extract(snmp_helper.snmp_get_oid((
        host, community, 161), oid_description))
    print('{:^30}'.format(host))
    print("System Name: {0}".format(host_name))
    print("System Description: {0}".format(host_description))
