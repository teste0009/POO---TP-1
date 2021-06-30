import base64
from db import dba
class Usuario ():
    def __init__(self, nombre,mail,password,celular):
        self.__id=0
        self.__nombre=nombre
        self.__mail=mail
        self.set_pass(password)
        self.__celular=celular
        self.__habilidades=[]

    

    def saludar(self):
        print(f"Hola {self.__nombre}")
    
    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre
    
    def get_mail(self):
        return self.__mail
    

    def get_pass(self):
        return self.__password
    
    def set_pass(self,password):
        self.__password=self.encriptarPass(password)
    
    def get_celular(self):
        return self.__celular
    
    def set_celular(self,celular):
        self.__celular=celular
    
    def set_id(self,id):
        self.__id=id
    
    def encriptarPass(self, password):
        return base64.encodebytes(bytes(password, 'utf-8')).decode('utf-8')
    
    def desencriptarPass(self,password):
        return base64.decodebytes(password.encode("UTF-8")).decode('utf-8')

    
    def MostrarTelefono(self):
        if self.__celular.get_marca()=="Apple":
            print(f" la marca es {self.__celular.get_marca()} y el proveedor es {self.__celular.get_proveedor()} y soy fanatico de apple")
        else:
            print(f" la marca es {self.__celular.get_marca()} y el proveedor es {self.__celular.get_proveedor()}")

    def llamar(self,usuario,tiempo):
        if self.__celular.get_proveedor()==usuario.get_celular().get_proveedor():
            return 0
        else:
            return tiempo*10
    
    def agregar_habilidad(self,habilidad):
        self.__habilidades.append(habilidad)
    
    def get_habilidades(self):
        return self.__habilidades
    
    def SabeHacer(self,habilidad,puntaje):
        resultado=0
        for i in self.__habilidades:
            if i.get_nombre().lower()==habilidad.lower() and puntaje<i.get_expertise():
                return True
        return False

    def save(self):
        sql="insert into usuarios (nombre,mail, password, celularID) values (%s,%s,%s,%s)"
        val=(self.get_nombre(), self.get_mail(), self.get_pass(), self.get_celular().get_id())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)

    def delete(self):
        sql="delete from usuarios where UsuarioID=%s"
        val=(self.get_id())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    



    


    


        


    
    
    
    

    