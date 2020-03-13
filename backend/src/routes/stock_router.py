from controllers.stock_controller import StockController
class StockRouter:

   def __init__(self, app, socket):
      self.app = app
      self.stockController = StockController(socket)
   
   def router(self):
      
      @self.app.route('/stock', methods=['GET'])
      def indexStock(): return self.stockController.index()
             
      pass