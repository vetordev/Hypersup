from flask import Flask, jsonify, request
from flask_socketio import SocketIO

from routes.sales_router import SalesRouter
from routes.stock_router import StockRouter
from routes.lote_router import LotRouter
from routes.product_router import ProductRouter
from routes.cashier_router import CashierRouter
from routes.shelf_router import ShelfRouter
from routes.safebox_router import SafeboxRouter
from routes.delivery_router import DeliveryRouter

from database.database import Database

from websocket.socket import Socket

class Server:

   def __init__(self, name):
      self.app = Flask(name)
      self.app.config['SECRET_KEY'] = 'secret!'
      self.socketio = SocketIO(self.app, cors_allowed_origins="*")
      
   def initRoutes(self):
      salesRouter = SalesRouter(self.app, self.socketio)
      salesRouter.router()

      stockRouter = StockRouter(self.app, self.socketio)
      stockRouter.router()

      lotRouter = LotRouter(self.app, self.socketio)
      lotRouter.router()

      productRouter = ProductRouter(self.app, self.socketio)
      productRouter.router()

      cashierRouter = CashierRouter(self.app, self.socketio)
      cashierRouter.router()

      shelfRouter = ShelfRouter(self.app, self.socketio)
      shelfRouter.router()

      safeboxRouter = SafeboxRouter(self.app, self.socketio)
      safeboxRouter.router()
      
      deliveryRouter = DeliveryRouter(self.app, self.socketio)
      deliveryRouter.router()
      pass
   def initSocket(self):
      socket = Socket(self.socketio, self.app)
      socket.run()

   def initDatabase(self, user, passwd, host, database):
      db = Database(user, passwd, host, database)
      db.connect()
      pass

   def run(self):
      self.app.debug = True
      self.socketio.run(self.app)
   

   