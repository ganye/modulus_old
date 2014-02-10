'''
Created on Feb 10, 2014

@author: ganye
'''
import os
import re

from core.command import Command
from lib.path import get_base_dir

class List(Command):
    
    about = "Lists the commands available in the modules directory. If given"
    about += " a subdirectroy as an argument, looks in that subdirectory."
    __validcallers__ = r"list"
    
    def callback(self, *args):
        found_items = []
        
        if not args:
            args = []
        
        # Convert args to a file path
        mod_path = '/modules'
        search_path = mod_path + '/'.join(args) + '/'
        
        # Remove any double /'s
        search_path = search_path.replace('//', '/')
        abs_path = get_base_dir() + search_path
        
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
            item_path = os.path.abspath(abs_path + item)
            if pattern.match(item) and not item.startswith("_"):
                item = item.replace(".py","")
                self.console.writeln("%s" % (search_path + item))
            elif os.path.isdir(item_path):
                self.console.writeln('%s/' % (search_path + item))