'''
Created on Feb 10, 2014

@author: ganye
'''
from core.command import Command

class Exit(Command):
    
    about = "Exits the program cleanly"
    __validcallers__ = "exit|quit"
    
    def callback(self, *args):
        self.console.exit()