#!/usr/bin/env python
from __future__ import print_function
import pyeapi
import argparse


'''
Functions
'''


def eAPI_results(output):
    return output[0]['result']


def checkVlan_exists(eAPI_Connection, vlanID):
    vlanID = str(vlanID)
    cmd = 'show vlan id {}'.format(vlanID)
    try:
        response = eAPI_Connection.enable(cmd)
        checkVlan = eAPI_results(response)['vlans']
        return checkVlan[vlanID]['name']
    except (pyeapi.eapilib.CommandError, KeyError):
        pass
    return False


def configureVlan(eAPI_Connection, vlanID, vlanName=None):
    commandString = 'vlan {}'.format(vlanID)
    cmd = [commandString]
    if vlanName is not None:
        commandString2 = 'name {}'.format(vlanName)
        cmd.append(commandString2)
    return eAPI_Connection.config(cmd)


'''
Define arguements
'''
parser = argparse.ArgumentParser()
parser.add_argument(
    'vlanID',
    action='store',
    help='VLAN (100-999)')
parser.add_argument(
    '--name',
    action='store',
    dest='vlanName',
    help='VLAN name')
parser.add_argument(
    '--remove',
    action='store_true',
    help='Remove VLAN')
args = parser.parse_args()


eAPI_Connection = pyeapi.connect_to('pynet-sw2')

vlanID = args.vlanID
remove = args.remove
vlanName = args.vlanName

checkVlan = checkVlan_exists(eAPI_Connection, vlanID)

if remove:
    if checkVlan:
        print('Removing existing VLAN')
        commandString = 'no vlan {}'.format(vlanID)
        eAPI_Connection.config([commandString])
    else:
        print('VLAN does not exist.')
else:
    if checkVlan:
        if vlanName is not None and checkVlan != vlanName:
            print('Setting VLAN name.')
            configureVlan(eAPI_Connection, vlanID, vlanName)
        else:
            print('VLAN already exists.')
    else:
        configureVlan(eAPI_Connection, vlanID, vlanName)
        print('VLAN added.')

