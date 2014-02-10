'''
Created on Feb 6, 2014

@author: xinv
'''
import os
import re

from lib.path import *

commands = {}

def list_commands():
    command_list = []
    files = os.listdir(os.path.join(get_base_dir(), 'commands'))
    pattern = re.compile(r'^.+\.py$')
    for file_ in files:
        if re.match(pattern, file_) and not file_.startswith('_'):
            command_list.append(file_)
            
def load_commands(command_list):
    global commands
    for command in command_list:
        module = __import__(("commands.%s" % command), fromlist=[command.title()])
        klass = getattr(module, command.title())
        valid = getattr(module, '__valid__')
        
        commands[re.compile('(%s' % valid)] = klass