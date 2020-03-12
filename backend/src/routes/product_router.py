from controllers.product_controller import ProductController
class ProductRouter:

   def __init__(self, app):
      self.app = app
   
   def router(self):
      
      @self.app.route('/product', methods=['GET'])
      def indexProduct(): return ProductController.index()
             
      pass