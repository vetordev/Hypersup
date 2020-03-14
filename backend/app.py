import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), 'src')))

import src.server

server = src.server.Server(__name__)
server.initDatabase('root', '', 'localhost', 'mercado')
server.initRoutes()
server.initSocket()
server.run()



