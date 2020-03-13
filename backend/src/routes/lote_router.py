from controllers.lote_controller import LotController
class LotRouter:

   def __init__(self, app, socket):
      self.app = app
      self.lotController = LotController(socket)
   
   def router(self):
      
      @self.app.route('/lot', methods=['GET'])
      def indexLot(): return self.lotController.index()
             
      pass