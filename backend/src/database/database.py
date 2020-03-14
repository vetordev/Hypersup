import mysql.connector

class Database:

   def __init__(self, user, passwd, host, database):
      self.user = user
      self.passwd = passwd
      self.host = host
      self.database = database

   def connect(self):
      self.connection = mysql.connector.connect(user=self.user, password=self.passwd, host=self.host, database=self.database)
      self.cursor = self.connection.cursor(dictionary=True)
      return self.connection
      pass
   
   def findAll(self, query):
      # Retorna todos os dados
      self.cursor.execute(query)
      return self.cursor.fetchall()
      pass

   def findOne(self):
      pass

   def insert(self):
      pass

   def update(self):
      pass

   def delete(self):
      pass