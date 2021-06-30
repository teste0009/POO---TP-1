import mysql.connector

dbconf={
  'host':'localhost',
  'user':'root',
  'password':'',
  'database':'usuarios'
}

class Db():
  def __init__(self):
    self.conexion=mysql.connector.Connect(**dbconf)
    self.cursor=self.conexion.cursor()

  def get_cursor(self):
    return self.cursor
  
  def get_conexion(self):
    return self.conexion


dba=Db()


