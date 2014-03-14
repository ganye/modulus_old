'''
Created on Mar 13, 2014

@author: ganye
'''
import os
import sys

from core.command import Command
from lib.path import get_base_dir

class Load(Command):
    about = "Loads the given module for configuration and usage."
    __validcallers__ = r"load"
    
    def callback(self, *args):
        if not args:
            self.console.error("'load' requires a module to load")
            return
        
        # Convert args to file path
        module_path = os.path.join('modules/', '/'.join(args))
        abs_path = os.path.join(get_base_dir(), module_path + '.py')
        
        if not os.path.isfile(abs_path) or module_path.split("/")[-1] == "__init__":
            self.console.error("module '%s' not found" % "/".join(args))
            return
        
        self.console.set_module(module_path)