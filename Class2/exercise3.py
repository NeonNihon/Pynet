#!/usr/bin/env python

from __future__ import print_function
from telnetlib import Telnet
import time
import socket
import sys

# For the purpose of this exercise static variable assignments.
ip_addr = '184.105.247.70'
username = 'pyclass'
password = '88newclass'


class TelnetDevice(object):
    '''
    Class details here
    '''

    def __init__(self, *args, **kwargs):
        self.ip_addr = kwargs.get('ip_addr')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.telnet_port = kwargs.get('telnet_port', 23)
        self.telnet_timeout = kwargs.get('telnet_timeout', 8)
        self.dev = {
            'ip': self.ip_addr,
            'username': self.username,
            'password': self.password,
            'telnet_port': self.telnet_port,
            'telnet_timeout': self.telnet_timeout
        }
        self._connect(self.dev)

    def _connect(self, *args, **kwargs):
        try:
            self.remote_conn = Telnet(
                self.ip_addr,
                self.telnet_port,
                self.telnet_timeout)
            self.output = self.remote_conn.read_until(
                'sername:', self.telnet_timeout)
            self.remote_conn.write(self.username + '\n')
            self.output += self.remote_conn.read_until(
                'ssword:', self.telnet_timeout)
            self.remote_conn.write(self.password + '\n')
            return self.remote_conn
        except socket.timeout:
            sys.exit('Connection timeout')

    def send_command(self, cmd, **kwargs):
        cmd = cmd.rstrip()
        self.remote_conn.write(cmd + '\n')
        time.sleep(1)
        return self.remote_conn.read_very_eager()

    def _close(self, *args, **kwargs):
        self.remote_conn.close()


def main():
    t = TelnetDevice(ip_addr=ip_addr, username=username, password=password)
    t.send_command('terminal length 0')
    print(t.send_command('show ip interface brief'))
    t._close()


if __name__ == '__main__':
    main()
