# coding: utf-8

import os
import sys
import configparser

__config_file__ = os.getenv('XSTORAGE_CONFIG_FILE', '%s/xstorageserver.ini' % os.getenv('HOME'))

# setting file read
config = configparser.ConfigParser()
if os.path.exists(__config_file__):
    config.read(__config_file__)

    if not config.has_section('APP'):
        sys.exit('no section APP')
    if not config.has_option('APP', 'DEBUG'):
        sys.exit('no option DEBUG in APP')
    if not config.has_option('APP', 'UPLOAD_FOLDER'):
        sys.exit('no option UPLOAD_FOLDER in APP')
else:
    sys.exit('config file not found: %s' % __config_file__)
