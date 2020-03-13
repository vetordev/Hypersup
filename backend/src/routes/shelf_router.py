from controllers.shelf_controller import ShelfController

class ShelfRouter:

   def __init__(self, app, socket):
      self.app = app
      self.shelfController = ShelfController(socket)
   
   def router(self):
      
      @self.app.route('/shelf', methods=['GET'])
      def indexShelf(): return self.shelfController.index()
             