'''
Created on Feb 5, 2014

@author: ganye
'''
from Queue import Queue
import sys
import os
import re

from core.excep import ModulusError
from core.colors import Color
from lib.path import get_base_dir

class Console(object):
    '''
    classdocs
    '''
    color = Color()
    commands = {}
    cursor = ">"
    current_module = None
    def __init__(self, istream=sys.stdin, ostream=sys.stdout, enable_colors=True):
        '''
        Constructor
        '''
        self.istream = istream
        self.ostream = ostream
        
        if not enable_colors:
            self.disable_color()
        
        self.load_commands()
        
    def write(self, output):
        self.ostream.write(output)
        
    def writeln(self, output):
        self.write(output + "\n")
        
    def readln(self):
        return self.istream.readline()
    
    def set_color(self, color):
        try:
            newcolor = getattr(self.color, color)
        except AttributeError:
            self.exception("invalid color '%s'" % color)
        else:
            self.write(newcolor)

    def disable_color(self):
        self.color.disable()
        
    def enable_color(self):
        self.color.enable()
            
    def debug(self, message):
        self.set_color("dark_blue")
        self.write("[*] debug: ")
        self.set_color("white")
        self.writeln("%s" % message)
            
    def exception(self, message):
        self.set_color('dark_red')
        self.write("[!!!] exception: ")
        self.set_color('white')
        self.writeln("%s" % message)
        
    def error(self, message):
        self.set_color('red')
        self.write("[!] error: ")
        self.set_color('white')
        self.writeln("%s" % message)
        
    def info(self, message):
        self.set_color('green')
        self.write('[+] ')
        self.set_color('white')
        self.writeln('%s' % message)
        
    def prompt(self):
        self.set_color('blue')
        self.write("%s " % self.cursor)
        if self.current_module:
            self.set_color('bold')
            self.write("(%s) " % self.current_module)
        self.set_color("white")
        
    def get_input(self):
        self.prompt()
        return self.readln()
    
    def handle_input(self, user_input):
        """
        TODO: clean this up; make it work.
        """
        user_input = user_input.split()
        user_command = user_input[0]
        args = user_input[1:]
        
        for pattern, command in self.commands.items():
            if pattern.match(user_command):
                run = command(self)
                run.caller(*args)
                return
        self.error("command '%s' not found." % user_command)
    
    def exit(self):
        sys.exit("Cleaning up...")
        
    def list_commands(self):
        command_list = []
        files = os.listdir(os.path.join(get_base_dir(), 'commands'))
        self.debug("Files: %s" % files)
        pattern = re.compile(r'^.+\.py$')
        for file_ in files:
            if re.match(pattern, file_) and not file_.startswith('_'):
                file_ = file_.split(".")[0]
                command_list.append(file_)
        return command_list
                
    def load_commands(self):
        command_list = self.list_commands()
        for command in command_list:
            self.debug("Importing %s..." % command)
            module = __import__(("commands.%s" % command), fromlist=[command.title()])
            klass = getattr(module, command.title())
            validcallers = getattr(klass, '__validcallers__')

            # import pdb; pdb.set_trace()
            self.commands[re.compile('%s' % validcallers)] = klass