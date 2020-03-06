from controllers.sales_controller import SalesController

class SalesRouter:

   def __init__(self, app):
      self.app = app
      
   
   def router(self):
      
      @self.app.route('/sales', methods=['GET'])
      def index(): return SalesControllers.index()
             
      pass