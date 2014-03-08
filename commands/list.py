'''
Created on Feb 10, 2014

@author: ganye
'''
import os
import re

from core.command import Command
from lib.path import *

class List(Command):
    
    about = "Lists the commands available in the modules directory. If given"
    about += " a subdirectroy as an argument, looks in that subdirectory."
    __validcallers__ = r"list"
    
    def callback(self, *args):
        found_items = []
        
        if not args:
            args = []
        
        modules_path = os.path.join('modules/')
        search_path = os.path.join(modules_path, '/'.join(args))
        abs_path = os.path.abspath(os.path.join(get_base_dir(), search_path))
        
        try:
            # Get a list of all directories and files
            for(dirpath, dirnames, filenames) in os.walk(abs_path):
                found_items.extend(dirnames)
                found_items.extend(filenames)
                break # break prevents going into subdirectories
        except OSError:
            self.console.error("'%s' is not a valid directory" % search_path)
            return
        
        pattern = re.compile(r"^.+\.py$")
        for item in found_items:
            # Get the absolute path for the item
            item_path = os.path.abspath(os.path.join(abs_path, item))
            if pattern.match(item) and not item.startswith("_"):
                item = item.replace(".py","")
                self.console.writeln("%s" % (os.path.join(search_path, item)))
            elif os.path.isdir(item_path):
                self.console.writeln('%s/' % (os.path.join(search_path, item)))