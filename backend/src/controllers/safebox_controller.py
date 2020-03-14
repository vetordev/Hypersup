from flask import jsonify
class SafeboxController:

   def __init__(self, socket, db):
      self.socket = socket
      self.db = db

   def index(self):
      query = 'select * from cofre'
      data = self.db.findAll(query)
      return jsonify(data)
      pass

   def show(self):
      pass

   def store(self):
      pass

   def update(self):
      pass

def destroy(self):
      pass
   