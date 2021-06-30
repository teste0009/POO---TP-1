from db import dba
class Celular():
    def __init__(self,marca,proveedor,modelo,numero):
        self.__id=0
        self.__marca=marca
        self.__proveedor=proveedor
        self.__modelo=modelo
        self.__numero=numero
    
    def get_marca(self):
        return self.__marca

    def get_proveedor(self):
        return self.__proveedor
    
    def get_numero(self):
        return self.__numero
    
    def get_modelo(self):
        return self.__modelo
    
    def get_id(self):
        return self.__id
    
    def set_id(self,id):
        self.__id=id
    
    def set_marca(self,marca):
        self.__marca=marca
    
    def set_proveedor(self,proveedor):
        self.__proveedor=proveedor
    
    def set_numero(self,numero):
        self.__numero=numero
    
    def set_modelo(self,modelo):
        self.__modelo=modelo
    
    def save(self):
        sql='insert into celular(marca,modelo,proveedor,numero) values(%s,%s,%s,%s)'
        val=(self.get_marca(),self.get_modelo(),self.get_proveedor(),self.get_numero())
        dba.cursor.execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)
    
    def delete(self):
        sql='delete from celular where CelularID=%s'
        val=(self.get_id(),)
        dba.cursor.execute(sql,val)
        dba.get_conexion().commit()
    
    def update(self,dic):
        sql="update celular set marca=%s, modelo=%s, proveedor=%s, numero=%s where CelularID=%s"
        val=(dic['marca'], dic['modelo'], dic['proveedor'],dic['numero'], self.get_id())
        dba.cursor.execute(sql,val)
        dba.get_conexion().commit()
        self.set_marca(dic['marca'])
        self.set_modelo(dic['modelo'])
        self.set_proveedor(dic['proveedor'])
        self.set_numero(dic['numero'])



    
