from flask import request
class Socket:

   def __init__(self, socket):
      self.socket = socket

   def run(self):
      @self.socket.on('connect')
      def connect():
         print('New Connection')
         print('Id: ${id}'.format(id=request.sid))

      