from flask import Flask, jsonify, request
from routes.SalesRouter import SalesRouter

class Server:

   def __init__(self, name):
      self.app = Flask(name)
      
   def initRoutes(self):
      salesRouter = SalesRouter(self.app)
      salesRouter.router()
      pass

   def initDatabase(self):
      pass

   def run(self):
      self.app.run(debug=True)
   

   