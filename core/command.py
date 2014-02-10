'''
Created on Feb 10, 2014

@author: ganye
'''

class Command(object):
    
    about = "Base Command object"
    __validcallers__ = "none"
    
    def __init__(self, console):
        self.console = console
    
    def caller(self, *args):
        if len(args) and args[0].lower() in ['help','?']:
            self.console.writeln(self.help())
        else:
            self.callback(*args)
    
    def callback(self, *args):
        raise NotImplementedError()
    
    @classmethod
    def help(cls):
        # Remove any escape characters
        cleancaller = cls.__validcallers__.replace('\\','')
        return "|-- %s%s" % (cleancaller.ljust(12), cls.about)