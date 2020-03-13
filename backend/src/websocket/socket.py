from flask import request
class Socket:

   def __init__(self, socket, app):
      self.socket = socket
      self.app = app

   def run(self):
      @self.socket.on('connect')
      def connect():
         print('New Connection; Id: ${id}'.format(id=request.sid))

      