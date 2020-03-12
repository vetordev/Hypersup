from controllers.shelf_controller import ShelfController

class ShelfRouter:

   def __init__(self, app):
      self.app = app
      
   
   def router(self):
      
      @self.app.route('/shelf', methods=['GET'])
      def indexShelf(): return ShelfController.index()
             