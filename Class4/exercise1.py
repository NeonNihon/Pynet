#!/usr/bin/env python
from __future__ import print_function
import paramiko
import time

ip_addr = '184.105.247.71'
username = 'pyclass'
password = '88newclass'
port = 22

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

remote_conn_pre.connect(
    ip_addr,
    username=username,
    password=password,
    look_for_keys=False,
    allow_agent=False,
    port=port)

remote_conn = remote_conn_pre.invoke_shell()
remote_conn.send('terminal length 0\n')
output = remote_conn.recv(5000)
remote_conn.send('show version\n')
time.sleep(1)
output = remote_conn.recv(65000)

print(output)
