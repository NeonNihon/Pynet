#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse


crypto_map = 'crypto map CRYPTO'
file = 'cisco_ipsec.txt'

conf_file = CiscoConfParse(file)

crypto = conf_file.find_objects(crypto_map)

for c in crypto:
    print(c.text)
    for child in c.children:
        print(child.text)

