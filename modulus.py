'''
Created on Feb 6, 2014

@author: xinv
'''
from core.console import Console

if __name__ == '__main__':
    console = Console()
    while True:
        user_input = console.get_input()
        console.handle_input(user_input)