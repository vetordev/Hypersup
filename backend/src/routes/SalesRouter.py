from controllers.SalesController import SalesController

class SalesRouter:

   def __init__(self, app):
      self.app = app
      print('ok')
   
   def router(self):
      
      
      @self.app.route('/sales', methods=['GET'])
      
      def index(): return sl.index()
         
         
      pass