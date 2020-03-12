from controllers.safebox_controller import SafeboxController

class SafeboxRouter:

   def __init__(self, app):
      self.app = app
      
   
   def router(self):
      
      @self.app.route('/safebox', methods=['GET'])
      def indexSafebox(): return SafeboxController.index()
             
      pass