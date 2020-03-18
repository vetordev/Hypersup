from flask import jsonify, request
from controllers.sales_controller import SalesController
class CashierController:

   def __init__(self, socket, db):
      self.socket = socket
      self.db = db
      
   def index(self):
      query = 'select * from caixa'
      data = self.db.findAll(query)
      return jsonify(data)

   def show(self):
      pass

   def store(self):

      #Efetuação da compra
         #INSERE PRIMEIRO EM VENDA
         #DEPOIS INSERE ITEM VENDA
         #DEPOIS INSERE NO CAIXA
      #Venda
      query = "INSERT INTO VENDA ..."
      self.db.insert(query)
      #ITEM
      query = "INSERT INTO ITEM..."
      self.db.insert(query)
      #CAIXA
      query = "INSERT INTO CAIXA ..."
      self.db.insert(query)

      #Reposição de produtos
         #Retirada da gondola -- melhor fazer com stored procedures
         # < 10 produtos na gondola -> reposição pelo estoque
         # < 1 lote no estoque -> notificar sistema web
      #GONDOLA
      query = "SELECT * FROM GONDOLA ..."
      products = 11 #self.db.findOne(query)
      if products < 10:
         #calculo pra pegar a qtd de produtos que faltam

         #Retira do estoque
         query = "UPDATE ESTOQUE SET ..."
         self.db.update(query)
         #Reposição da gondola
         query = "UPDATE GONDOLA SET ..."
         self.db.update(query)
         pass
      #ESTOQUE
      query = "SELECT * FROM ESTOQUE ..."
      estoque = 0.5 #self.db.findOne(query)
      # calc
      if estoque < 1:
         #Emitir uma notificação pro sistema web
         self.socket.emit('without_stock', {'stock': estoque} )
         return jsonify('EMIT')
         pass

      
      pass
   

   def update(self):
      pass

   def destroy(self):
      pass
   