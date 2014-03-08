'''
Created on Feb 6, 2014

@author: xinv
'''
import os
import re

__all__ = ['get_base_dir','get_file_path','get_dir_path',]

def get_base_dir():
    return os.path.dirname(os.path.dirname(__file__))

def get_file_path(*args):
    pattern = re.compile('/+')
    path = []
    for arg in args:
        path.append('/' + arg)

    path = ''.join(path).replace('//','/').rstrip('/')
    
    while '//' in path:
        path = path.replace('//','/')
    
    return path

def get_dir_path(*args):
    return get_file_path(*args) + '/'