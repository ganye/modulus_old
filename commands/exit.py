'''
Created on Feb 10, 2014

@author: ganye
'''
from core.command import Command

__validcallers__ = "exit|quit"

class Exit(Command):
    def callback(self, args):
        self.console.exit()
        
    @staticmethod
    def help():
        return "Exits the program cleanly."