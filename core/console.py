'''
Created on Feb 5, 2014

@author: ganye
'''
from Queue import Queue
import sys

from core.colors import Color

class Console(object):
    '''
    classdocs
    '''
    color = Color()
    cursor = ">"
    current_module = None
    def __init__(self, istream=sys.stdin, ostream=sys.stdout):
        '''
        Constructor
        '''
        self.istream = istream
        self.ostream = ostream
        self.stack = Queue()
        
    def write(self, output):
        self.ostream.write(output)
        
    def writeln(self, output):
        self.istream.write(output + "\n")
        
    def readln(self):
        return self.istream.readline()
    
    def set_color(self, color):
        try:
            newcolor = getattr(self.color, color)
        except AttributeError:
            self.exception("invalid color '%s'" % color)
        else:
            self.write(newcolor)
            
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