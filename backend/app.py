import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), 'src')))

import src.server

server = src.server.Server(__name__)
server.initRoutes()
server.initDatabase('root', '', 'localhost', 'devdb')
server.run()



