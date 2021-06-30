from db import dba
from validate_email import validate_email
import base64
class Validador():
    def __init__(self):
        pass

    def validar_celular(self,dicc):
        datosFinales={}
        errores={}
        for x,y in dicc.items():
            datosFinales[x]=y.strip()
        
        if datosFinales['marca']=='':
            errores['marca']='campo marca vacio'
        
        if datosFinales['modelo']=='':
            errores['modelo']='campo modelo vacio'

        if datosFinales['proveedor']=='':
            errores['proveedor']='campo proveedor vacio'
        
        if datosFinales['numero']=='':
            errores['numero']='campo numero vacio'
        elif datosFinales['numero'].isdigit()==False:
            errores['numero']="el campo contiene letras"
        if errores=={}:
            sql="select CelularID from celular where numero=%s"
            val=(datosFinales['numero'],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores['Numero']='El numero ya esta registrado en nuestra base'
                return errores
        return errores

    def validar_usuario(self,dicc):
        datosFinales={}
        errores={}
        carcteresEspeciales=['$','@','#','%']
        for x,y in dicc.items():
            datosFinales[x]=y.strip()
        
        if datosFinales['nombre']=='':
            errores['nombre']='campo nombre vacio'
        
        if datosFinales['mail']=='':
            errores['mail']='campo mail vacio'
        elif validate_email(datosFinales["mail"])==False:
            errores["mail"]="No tiene el formato de email"
        
        if len(datosFinales["password"])<6:
            erorres['password']="la password debe contener mas de 6 caracteres"
        elif datosFinales['password']=='':
            errores['password']='campo password vacio'
        elif not any(i.isupper() for i in datosFinales["password"]):
            errores["password"]="Password debe contener una letra mayuscula"
        elif not any(i.isdigit() for i in datosFinales["password"]):
            errores["password"]="Password debe contener un caracter numeral"
        elif not any(i.islower() for i in datosFinales["password"]):
            errores["password"]="Password debe contener una letra minuscula"
        elif not any(i in carcteresEspeciales for i in datosFinales["password"]):
            errores["password"]="Password debe contener carateres especiales $@#"
        
        if errores=={}:
            sql="select UsuarioID from usuarios where mail=%s"
            val=(datosFinales['mail'],)
            dba.get_cursor().execute(sql,val)
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores['mail']='El mail ya esta registrado'
                return errores
        return errores

    def validar_login(self,dic):
        sql="select * from usuarios where mail=%s"
        val=(dic['mail'],)
        dba.get_cursor().execute(sql,val)
        result=dba.get_cursor().fetchone()
        if result==[]:
            return False
        if base64.decodebytes(result[3].encode("UTF-8")).decode('utf-8')==dic['password']:
            return result
        else:
            return False
        

        



        
        

        

        
        

val= Validador()