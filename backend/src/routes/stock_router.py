from controllers.stock_controller import StockController
class StockRouter:

   def __init__(self, app):
      self.app = app
   
   def router(self):
      
      @self.app.route('/stock', methods=['GET'])
      def indexStock(): return StockController.index()
             
      pass