'''
Created on Feb 5, 2014

@author: ganye
'''
import socket
import struct
import fcntl

def get_mac_address(ifname):
    """
    Returns the MAC address for a given interface.
    >>> get_mac_address('eth0')
    00:00:de:ad:be:ef
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927, struct.pack('256s', ifname[:15]))
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]