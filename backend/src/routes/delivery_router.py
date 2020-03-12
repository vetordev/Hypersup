from controllers.delivery_controller import DeliveryController

class DeliveryRouter:

   def __init__(self, app):
      self.app = app
      
   
   def router(self):
      
      @self.app.route('/delivery', methods=['GET'])
      def indexDelivery(): return DeliveryController.index()
             