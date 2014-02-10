'''
Created on Feb 10, 2014

@author: ganye
'''
from core.command import Command

class Help(Command):
    
    about = "Displays information for all commands"
    __validcallers__ = r"help|\?"
    
    def callback(self, *args):
        commands = self.console.commands.values()
        for command in commands:
            self.console.writeln(command.help())

        