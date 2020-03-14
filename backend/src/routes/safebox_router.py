from controllers.safebox_controller import SafeboxController

class SafeboxRouter:

   def __init__(self, app, socket, db):
      self.app = app
      self.safeboxController = SafeboxController(socket, db)
      
   
   def router(self):
      
      @self.app.route('/safebox', methods=['GET'])
      def indexSafebox(): return self.safeboxController.index()
             
      pass