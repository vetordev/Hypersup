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
      salesRouter = SalesRouter(self.app)
      salesRouter.router()

      stockRouter = StockRouter(self.app)
      stockRouter.router()

      lotRouter = LotRouter(self.app)
      lotRouter.router()

      productRouter = ProductRouter(self.app)
      productRouter.router()

      cashierRouter = CashierRouter(self.app)
      cashierRouter.router()

      shelfRouter = ShelfRouter(self.app)
      shelfRouter.router()

      safeboxRouter = SafeboxRouter(self.app)
      safeboxRouter.router()
      
      deliveryRouter = DeliveryRouter(self.app)
      deliveryRouter.router()
      pass
   def initSocket(self):
      socket = Socket(self.socketio)
      socket.run()

   def initDatabase(self, user, passwd, host, database):
      db = Database(user, passwd, host, database)
      db.connect()
      pass

   def run(self):
      self.app.debug = True
      self.socketio.run(self.app)
   

   