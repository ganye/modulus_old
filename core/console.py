'''
Created on Feb 5, 2014

@author: ganye
'''
import traceback
import sys
import os
import re

from core.colors import Color
from lib.path import get_base_dir
from lib.sysinfo import is_windows

class Console(object):
    '''
    classdocs
    '''
    color = Color()
    commands = {}
    cursor = ">"
    current_module = None
    def __init__(self, istream=sys.stdin, ostream=sys.stdout, colors=True):
        '''
        Constructor
        '''
        self.istream = istream
        self.ostream = ostream
        
        if not colors or is_windows():
            self.disable_color()
            self.debug('disabling colors...')
        
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
            
    def warning(self, message):
        self.set_color("purple")
        self.write("[!] warning: ")
        self.set_color("white")
        self.writeln("%s" % message)
            
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

            self.commands[re.compile('%s' % validcallers)] = klass
            
    def set_module(self, new_module):
        name = new_module.split("/")[-1]
        # Replace forward slashes with dots for importing
        module_path = new_module.replace("/", ".")
        # Strip the first dot
        module_path = module_path.lstrip(".")
        
        # Load the actual module class
        try:
            module = __import__(module_path, fromlist=[name])
        except SyntaxError, e:
            self.exception("module contains a syntax error and cannot be loaded")
            traceback.print_exc(e)
            return
        
        try:
            name = getattr(module, '__module__')
        except AttributeError:
            self.warning("module does not contain a __module__ attribute - " \
                "defaulting to %s" % name.title())
            name = name.title()
            
        klass = getattr(module, name)
        
        self.module = klass(self)
        self.current_module = new_module