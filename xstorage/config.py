# coding: utf-8

import os
import sys
import ConfigParser

default_file = '%s/xstorage.ini' % os.getenv('HOME')

config_file = os.getenv('XSTORAGE_CONFIG_FILE', default_file)

# current_path = os.path.dirname(os.path.abspath(__file__))

# setting file read
config = ConfigParser.ConfigParser()
if os.path.exists(config_file):
    config.read(config_file)
else:
    sys.exit('config file not found: %s' % config_file)
