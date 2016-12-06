#!/usr/bin/env python
from __future__ import print_function
import paramiko
import time


def send_cmd(conn, cmd, buff=5000):
    conn.send(cmd)
    time.sleep(1)
    output = conn.recv(buff)
    return output


ip_addr = '184.105.247.71'
username = 'pyclass'
password = '88newclass'
port = 22
buffer_size = input('New buffer size: ')

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
send_cmd(remote_conn, 'terminal length 0\n')
send_cmd(remote_conn, 'configure terminal\n')
send_cmd(remote_conn, 'logging buffered {0}\n'.format(buffer_size))
print('logging buffered is now {0}.'.format(buffer_size))
