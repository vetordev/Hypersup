from flask import Flask, jsonify, request
from routes.sales_router import SalesRouter
from database.database import Database

class Server:

   def __init__(self, name):
      self.app = Flask(name)
      
   def initRoutes(self):
      salesRouter = SalesRouter(self.app)
      salesRouter.router()
      pass

   def initDatabase(self, user, passwd, host, database):
      db = Database(user, passwd, host, database)
      db.connect()
      pass

   def run(self):
      self.app.run(debug=True)
   

   