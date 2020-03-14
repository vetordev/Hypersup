from controllers.product_controller import ProductController
class ProductRouter:

   def __init__(self, app, socket, db):
      self.app = app      
      self.productController = ProductController(socket, db)

   def router(self):
   
      @self.app.route('/product', methods=['GET'])
      def indexProduct(): return self.productController.index()
             
      pass