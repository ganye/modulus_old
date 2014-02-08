'''
Created on Feb 6, 2014

@author: xinv
'''
import os

__all__ = ['get_base_dir',]

def get_base_dir():
    return os.path.dirname(os.path.dirname(__file__))