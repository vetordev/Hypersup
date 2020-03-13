from flask import jsonify
class ShelfController:

   def __init__(self, socket):
      self.socket = socket

   def index(self):
      return jsonify('OK')
      pass
   
   def show(self):
      pass
   
   def store(self):
      pass

   def update(self):
      pass

   def destroy(self):
      pass