from flask import jsonify

class CashierController:

   def __init__(self, socket, db):
      self.socket = socket
      self.db = db
      
   def index(self):
      query = 'select * from caixa'
      data = self.db.findAll(query)
      return jsonify(data)

   def show(self):
      pass

   def store(self):
      pass

   def update(self):
      pass

   def destroy(self):
      pass
   