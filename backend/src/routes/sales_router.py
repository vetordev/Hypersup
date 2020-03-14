from controllers.sales_controller import SalesController

class SalesRouter:

   def __init__(self, app, socket, db):
      self.app = app
      self.salesController = SalesController(socket, db)
   
   def router(self):
      
      @self.app.route('/sales', methods=['GET'])
      def indexSales(): return self.salesController.index()
             
      pass