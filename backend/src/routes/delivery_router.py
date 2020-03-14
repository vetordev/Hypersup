from controllers.delivery_controller import DeliveryController

class DeliveryRouter:

   def __init__(self, app, socket, db):
      self.app = app
      self.deliveryController = DeliveryController(socket, db)
      
   
   def router(self):
      
      @self.app.route('/delivery', methods=['GET'])
      def indexDelivery(): return self.deliveryController.index()
             