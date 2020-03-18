from controllers.item_controller import ItemController
class ItemRouter:

   def __init__(self, app, socket, db):
      self.app = app
      self.itemController = ItemController(socket, db)
   
   def router(self):
      
      @self.app.route('/item', methods=['GET'])
      def indexItem(): return self.itemController.index()
             
      pass