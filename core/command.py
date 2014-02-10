'''
Created on Feb 10, 2014

@author: ganye
'''
from functools import wraps

class Command(object):
    def __init__(self, console):
        self.console = console
    
    def caller(self, *args):
        import pdb; pdb.set_trace()
        if len(args) and args[0].lower() in ['help','?']:
            self.help()
        else:
            self.callback(*args)
    
    def callback(self, *args):
        raise NotImplementedError()
    
    @staticmethod
    def help():
        raise NotImplementedError()