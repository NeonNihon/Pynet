#!/usr/bin/env python
from __future__ import print_function
import pyeapi


def pyeapi_result(output):
    return output[0]['result']


eapi_conn = pyeapi.connect_to("pynet-sw2")

interfaces = eapi_conn.enable("show interfaces")
interfaces = pyeapi_result(interfaces)

interfaces = interfaces['interfaces']

stats = {}
for interface, intValues in interfaces.items():
    intCounters = intValues.get('interfaceCounters', {})
    stats[interface] = (intCounters.get(
        'inOctets'), intCounters.get('outOctets'))

print("\n{:20} {:<20} {:<20}".format(
    "Interface:", "inOctets", "outOctets"))
for stat, octets in stats.items():
    print("{:20} {:<20} {:<20}".format(stat, octets[0], octets[1]))
