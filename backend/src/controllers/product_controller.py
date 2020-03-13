from flask import jsonify
class ProductController:

   def __init__(self, socket):
      self.socket = socket
      
   def index(self):
      self.socket.emit('product', {'product' : '0001'})
      return jsonify('GO')
      pass

   def show(self):
      pass

   def store(self):
      pass

   def update(self):
      pass

   def destroy(self):
      pass