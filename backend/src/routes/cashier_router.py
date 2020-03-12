from controllers.cashier_controller import CashierController

class CashierRouter:

   def __init__(self, app):
      self.app = app
      
   
   def router(self):
      
      @self.app.route('/cashier', methods=['GET'])
      def indexCashier(): return CashierController.index()
             