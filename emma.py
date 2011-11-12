#!/usr/env/python
"""
Author: Andy Nagels
Date: 2011-11-12
Emma: Equations for Money Management

Copyright (C) 2010 Andy Nagels

This file is part of Emma.

Emma is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Emma is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Emma. If not, see <http://www.gnu.org/licenses/>.
					
"""
import getopt
import sys
from mdlprocess import Process
from mdlconfig import ConfigParser
        
class MainWrapper():
    """ Main logic 
    
    Parsed options get there functionality here.
    
    """ 

    def __init__(self, parent=None):
        """ Init. """
        # general properties of the app
        self.pprog = 'Emma.py'
        self.pversion = '0.01'
        self.prelease = 'I Want Some Mushu!'
        self.pdate = '2011-11-12'
        self.exitstate = 0   
        # config
        self.config = ConfigParser()
    
    def usage(self):
        """ Print usage info and exit """
        print('''{0} : Equations for Money Management Application
Options (buy): 
 -C <Capital (total pool)>
 -u <used (traded capital)>
 -t <tax>
 -c <commission>
 -p <price>
 [-r <risk percentage>] (default: 2)
 [-s <sell price>] (default: -1)
 [-a <amount you sell>]
Options (general):
 --verbose, -v : verbose mode
 --help, -h : displays this help message
 --version : displays version
 --python : displays Python version '''.format(self.pprog))

    def run(self):
        """ This is the main driver for the program. """
        if self.exitstate == 1:
            sys.exit(0)
        # run the data processing
        myapp = Process(self.config)
        myapp.buy()
        exit(0)

def main():
    """ Main driver, startup and cli options parsing. """
    # Gonna switch this to optparse later
    try:
        options, xarguments = getopt.getopt(
                sys.argv[1:], 'C:t:c:p:r:s:a:h', ['version', 'python'])
    except getopt.error as err:
        print('Error: ' + str(err))
        sys.exit(1)
    wrapper = MainWrapper()
    
    if len(options) == 0:
        wrapper.usage()
        wrapper.exitstate = 1

    for opt, arg in options:
        if opt in ('-h','--help'):
            wrapper.usage()
            # don't run the program after the optionparsing
            wrapper.exitstate = 1
        elif opt in ('-V', '--version'):
            str_list = [
                wrapper.pprog,
                ' version ',
                wrapper.pversion,
                ' (',
                wrapper.pdate,
                '), \'',
                wrapper.prelease,
                '\' release.']
            print(''.join(str_list))
            wrapper.exitstate = 1
        elif opt in ('--python'):
            print('Python ' + sys.version)
            wrapper.exitstate = 1

    wrapper.run() #run the main method for the program

if __name__ == "__main__":
    main()
