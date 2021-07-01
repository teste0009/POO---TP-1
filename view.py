import os
from usuario import Usuario
from constantes import *


class View():
  def __init__(self) -> None:
    self.__cant_opciones = 0
    self.__menu = {
      PF_INVITADO: ["Ver Productos", "Login", "Registrarse"],
      PF_USUARIO: ["Mi carrito", "Ver, Comprar Productos", "Mis Datos", "Logout"],
      PF_ADMIN: ["Categorias", "Marcas", "Productos", "Usuarios", "Resumen Carritos", "Logout"]
    }
    self.__str_nombre_usuario = ""

  def get_cant_opciones(self) -> int:
    return self.__cant_opciones

  def get_menu(self) -> dict:
    return self.__menu

  def __borrar_pantalla(self):
    borrarPantalla = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    borrarPantalla()

  def mostrar_mensajes(self, d_mensajes:dict):
    print()
    for str_tipo, _mensajes in d_mensajes.items():
      for str_mensaje in _mensajes:
        print(f"{str_tipo}: {str_mensaje}.")

  def titulo_menu(self, titulo:str):
    self.__borrar_pantalla()
    print("* * Curso POO - TP 1 - Ecommerce * *\n")
    print(f"{titulo}: {self.__str_nombre_usuario}")
    print("-" * (len(titulo) + 1)) # + len(self.__str_nombre_usuario) + 2))

  def menu_principal(self, _perfil_menu_usuario:list, d_mensajes:dict):
    str_perfil, self.__str_nombre_usuario = _perfil_menu_usuario[0], _perfil_menu_usuario[1]
    self.__cant_opciones = len(self.__menu[str_perfil])

    cont = 1
    self.titulo_menu("Menú principal")
    for opcion in self.__menu[str_perfil]:
      print(f"{cont} - {opcion}.")
      cont += 1
    print("\n0 - Salir.")

    self.mostrar_mensajes(d_mensajes)

  def listar_productos(self, _productos:list, b_admin:bool=False):
    ancho = 18
    print("ID.".center(5), end="") if (b_admin) else print("Num".center(5), end="")
    print("Categoria".center(ancho), "Marca".center(ancho), "Descripción".center(ancho*2), "Precio".center(10))
    for i in range(len(_productos)):
      _producto = _productos[i]
      print(str(_producto[0]).center(5), end="") if (b_admin) else print(str(i+1).center(5), end="")
      print(_producto[1].ljust(ancho), _producto[2].ljust(ancho), _producto[3].ljust(ancho*2), str(_producto[4]).rjust(10))
    print() if (b_admin) else None

  def listar_compras(self, _compras:list, total:float):
    print("Num".center(5), "Cant:".center(5), "Descripción".center(40), "Precio".center(10))
    for i in range(len(_compras)):
      _compra = _compras[i]
      print(str(i+1).center(5), (str(_compra[1])+' x').center(5), _compra[2].ljust(40), str(_compra[3]).rjust(10))
    print("\nValor Total del Carrito: ", total, "\n")
    print(str(len(_compras)+1).center(5), "Finalizar Compra.")

  def mostrar_datos_usuario(self, _usuario:Usuario, _carritos:list):
    print(f"DNI:       {_usuario.get_dni()}")
    print(f"Nombre:    {_usuario.get_nombre()}")
    print(f"Email:     {_usuario.get_email()}")
    print(f"Ciudad:    {_usuario.get_ciudad()}")
    print(f"Provincia: {_usuario.get_provincia()}")
    print(f"Pais:      {_usuario.get_pais()}\n")
    print(f"Carritos comprados:".ljust(21), f"{str(_carritos[2]).rjust(2)}. Total: {str(_carritos[3]).rjust(10)}.")
    print(f"Carritos pendientes:".ljust(21), f"{str(_carritos[0]).rjust(2)}. Total: {str(_carritos[1]).rjust(10)}.\n")

  def listado_generico(self, _registros:list):
    print("ID.".center(6), "Nombre".ljust(30))
    for _registro in _registros:
      id, nombre = _registro
      print(str(id).center(6), nombre.ljust(30))
    print()

  def listar_usuarios(self, _usuarios:list):
    print("ID.".center(5), "DNI".ljust(10), "Nombre".ljust(20), "Email".ljust(20), "Password".ljust(10), "Admin".ljust(6), "Ciudad".ljust(15), "Provincia".ljust(15), "País".ljust(15))
    for _usr in _usuarios:
      print(str(_usr[0]).center(5), str(_usr[1]).ljust(10), _usr[2].ljust(20), _usr[4].ljust(20), _usr[7].ljust(10), _usr[8].ljust(6), _usr[9].ljust(15), _usr[10].ljust(15), _usr[11].ljust(15))
    print()

  def resumen_carritos(self, _carritos:list):
    print("Usuario".ljust(15), "Comprado", "Carritos", "Total".rjust(10), "Productos")
    for _carrito in _carritos:
      print(_carrito[0].ljust(15), _carrito[1].center(8), str(_carrito[2]).center(8), str(_carrito[3]).rjust(10), str(_carrito[4]).center(9))
    print()