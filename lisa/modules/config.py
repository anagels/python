#! /usr/local/bin/python
"""
This file is part of Lisa.

Lisa is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Lisa is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Lisa. If not, see <http://www.gnu.org/licenses/>.
					
"""
import configparser

class ConfigParser():
    """ Class that contains values from the config file. """

    def __init__(self):
        """ Initialise config class. """ 
        self.myconf = 'config/lisa.rc'
        self.dbhost = ''
        self.dbname = ''
        self.dbuser = ''
        self.dbpass = ''
        self.importdir = ''
        self.exportdir = ''
        self.logfile = ''
        self.default_tax = ''
        self.default_risk = ''
        self.default_currency = ''
        self.default_exchange_rate = ''
        self.config()
 
    def config(self):
        """ Retrieve config file values """
        config = configparser.RawConfigParser()
        config.read(self.myconf)
        
        self.dbhost = config.get('database', 'host')[1:-1]
        self.dbname = config.get('database', 'name')[1:-1]
        self.dbuser = config.get('database', 'user')[1:-1]
        self.dbpass = config.get('database', 'password')[1:-1]
        self.importdir = config.get('data', 'importdir')[1:-1]
        self.exportdir = config.get('data', 'exportdir')[1:-1]
        self.default_tax = config.get('data', 'default_tax')[1:-1]
        self.default_risk = config.get('data', 'default_risk')[1:-1]
        self.default_currency = config.get('data', 'default_currency')[1:-1]
        self.default_exchange_rate = config.get('data', 'default_exchange_rate')[1:-1]
        self.logfile = config.get('logging', 'logfile')[1:-1]
