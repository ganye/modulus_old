'''
Created on Feb 5, 2014

@author: ganye
'''
import lib.network
import unittest


class Test(unittest.TestCase):
    def testMAC(self):
        self.assertEquals(lib.network.get_mac_address('eth0'),
                          '08:60:6e:0c:1a:ff')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMAC']
    unittest.main()