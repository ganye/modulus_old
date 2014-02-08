'''
Created on Feb 6, 2014

@author: xinv
'''

class ModulusError(Exception):
    '''
    Exception object used by modulus
    '''
    def __init__(self, error):
        self.error = error
        
    def __repr__(self):
        return "%s" % self.error

    def __str__(self):
        return repr(self.error)
        