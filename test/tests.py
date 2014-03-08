'''
Created on Feb 5, 2014

@author: ganye
'''
import lib.path
import unittest


class Test(unittest.TestCase):
    def test_file_path(self):
        self.assertEqual(lib.path.get_file_path('dev','null'), '/dev/null')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMAC']
    unittest.main()