import mysql.connector

class Database:

   def __init__(self, user, passwd, host, database):
      self.user = user
      self.passwd = passwd
      self.host = host
      self.database = database

   def connect(self):
      self.connection = mysql.connector.connect(user=self.user, password=self.passwd, host=self.host, database=self.database)
      return self.connection
      pass
   
   def findAll():
      pass

   def findOne():
      pass

   def insert():
      pass

   def update():
      pass

   def delete():
      pass