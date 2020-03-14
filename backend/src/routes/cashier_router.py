from controllers.cashier_controller import CashierController

class CashierRouter:

   def __init__(self, app, socket, db):
      self.app = app
      self.cashierController = CashierController(socket, db)
   
   def router(self):
      
      @self.app.route('/cashier', methods=['GET'])
      def indexCashier(): return self.cashierController.index()
             