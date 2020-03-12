from controllers.lote_controller import LotController
class LotRouter:

   def __init__(self, app):
      self.app = app
   
   def router(self):
      
      @self.app.route('/lot', methods=['GET'])
      def indexLot(): return LotController.index()
             
      pass