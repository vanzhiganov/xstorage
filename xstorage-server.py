#!/usr/bin/env python

from xStorageServer.application import init_app

if __name__ == '__main__':
    app = init_app()
    app.run()
