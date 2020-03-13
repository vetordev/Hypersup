from controllers.cashier_controller import CashierController

class CashierRouter:

   def __init__(self, app, socket):
      self.app = app
      self.cashierController = CashierController(socket)
   
   def router(self):
      
      @self.app.route('/cashier', methods=['GET'])
      def indexCashier(): return self.cashierController.index()
             