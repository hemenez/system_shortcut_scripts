#!/usr/bin/python3
import sys
import os
import subprocess

def find_easterEgg():
    ''' Function finds a file in your home dir
    when you don't remember it's location.
    Function also has capability to search by keyword

    To use: add script to /usr/bin
    Usage: `file_finder.py ea`
    Will return: all files containing `ea` and their
    location in your home directory
    '''
    if len(sys.argv) == 1:
        return print("Please specify a term to search for")
    if len(sys.argv[1]) < 2:
        return print("Please specify a search file with more than one letter")
    file_name = "*" + sys.argv[1] + "*"
    home_dir = os.path.expanduser('~/')
    command = "find " + home_dir + " -name " + file_name + " -type f"
    try:
        my_output = subprocess.check_output(command, shell=True)
        if len(my_output) > 1:
            print(my_output.decode().replace(os.path.expanduser('~/'), '~/'), end="")
        else:
            raise FileNotFoundError
    except (FileNotFoundError, subprocess.CalledProcessError):
        print('File not found')

find_easterEgg()
