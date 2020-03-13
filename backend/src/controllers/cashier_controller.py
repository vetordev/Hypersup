from flask import jsonify
class CashierController:

   def __init__(self, socket):
      self.socket = socket

   def index(self):
      return jsonify('Go')
      pass

   def show(self):
      pass

   def store(self):
      pass

   def update(self):
      pass

   def destroy(self):
      pass
   