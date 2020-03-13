from controllers.delivery_controller import DeliveryController

class DeliveryRouter:

   def __init__(self, app, socket):
      self.app = app
      self.deliveryController = DeliveryController(socket)
      
   
   def router(self):
      
      @self.app.route('/delivery', methods=['GET'])
      def indexDelivery(): return self.eliveryController.index()
             