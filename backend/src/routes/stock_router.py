from controllers.stock_controller import StockController
class StockRouter:

   def __init__(self, app, socket, db):
      self.app = app
      self.stockController = StockController(socket, db)
   
   def router(self):
      
      @self.app.route('/stock', methods=['GET'])
      def indexStock(): return self.stockController.index()
             
      pass