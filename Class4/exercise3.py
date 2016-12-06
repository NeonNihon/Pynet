#!/usr/bin/env python
from __future__ import print_function
import pexpect

ip_addr = '184.105.247.71'
username = 'pyclass'
password = '88newclass'
port = 22

ssh_conn = pexpect.spawn(
    'ssh {0} -l {1} -p {2}'.format(
        ip_addr, username, port))
ssh_conn.timeout = 3
ssh_conn.expect('ssword:')
ssh_conn.sendline(password)

ssh_conn.expect('#')

ssh_conn.sendline('show ip interface brief')
ssh_conn.expect('#')

print(ssh_conn.before)

ssh_conn.close()
