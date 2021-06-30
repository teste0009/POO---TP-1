from usuario import Usuario
from celular import Celular
from habilidad import Habilidad
from validador import val




#celular2=Celular("Apple","Claro","112783434")



#usuario2=Usuario("federico","federico.croci@mail.com", "jfhdjfsdsdsdahdjfhud",celular2)
"""
habilidad1=Habilidad("Correr",4)

habilidad2=Habilidad("comer",3)

habilidad3=Habilidad("saltar",4)

usuario1.agregar_habilidad(habilidad1)
usuario1.agregar_habilidad(habilidad2)
usuario1.agregar_habilidad(habilidad3)
celular1=Celular("Y","Claro",'Y 20',"112233434")
celular1.save()
usuario1=Usuario("lucas","lucas.croci@mail.com", "hola123",celular1)
usuario1.save()"""

"""
update={}
update['marca']="moto"
update['modelo']="XZ"
update['proveedor']="claro"
update['numero']= "4477884411"

usuario={}
usuario['nombre']="lucas"
usuario['mail']="lucas@bue.edu.ar"
usuario['password']="dsWdada$2

login={'mail':"lucas.croci@mail.com","password":"hola123"}"""

def registracion_celular():
    i=False
    while not i==True:

        datos={}
        datos["marca"]=input("Ingrese la marca:\n")
        datos["modelo"]=input("Ingrese modelo de celular:\n")
        datos["proveedor"]=input("ingrese proveedor:\n")
        datos["numero"]=input("ingrese numero:\n")
        errores=val.validar_celular(datos)
        if not errores:
            cel=Celular(**datos)
            cel.save()
            print(" Se regitro el celular Correctamente")
            return cel
            i==True
        for i in errores.values():
            print(i)

def registracion_usuario(celular):
    i==False
    while not i==True:
        datos={}
        datos["nombre"]=input("Ingrese su nombre:\n")
        datos["mail"]=input("Ingrese un mail:\n")
        datos["password"]=input("ingrese password:\n")
        datos["cpassword"]=input("Confirmacion de password:\n")
        errores=val.validar_usuario(datos)
        if not errores:
            datos["celular"]=celular
            datos["id"]=0
            del datos["cpassword"]
            user=Usuario(**datos)
            user.save()
            i==True
            return user
        [print(i) for i in errores.values()]
"""
celular1=Celular("Y","Claro",'Y 20',"112778434")
registracion_usuario(celular1)"""

def login():
    datos={}
    datos['mail']=input("ingrese su email\n")
    datos["password"]=input("ingrese password:\n")
    errores=val.validar_login(datos)
    if  isinstance(errores, tuple):
        user=Usuario(errores[1],errores[2],errores[3],errores[4])
        user.set_id(errores[0])
        return user.get_id()

    return errores


user={'mail':'lucasfederico@mail.com','password':'Hola123$'}

print(login())














