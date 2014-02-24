'''
Created on Feb 6, 2014

@author: xinv
'''
import argparse
import sys

from core.console import Console

def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--disable-colors', help='Disables text colors.',
                        action='store_true')
    parser.add_argument('-i', '--input-file',
                        help='File to read commands and input from.')
    parser.add_argument('-o', '--output-file', 
                        help='File to write output to.')
    return parser.parse_args()

if __name__ == '__main__':
    args = args_parse()
    
    if args.input_file:
        istream = args.input_file
    else:
        istream = sys.stdin
        
    if args.output_file:
        ostream = args.output_file
    else:
        ostream = sys.stdout
    
    colors = not args.disable_colors
    
    console = Console(istream=istream, ostream=ostream, colors=colors)
    while True:
        user_input = console.get_input()
        console.handle_input(user_input)