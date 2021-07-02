from ui import UI # Interface de Usuario
from validador import Validador
from usuario import Usuario
from carrito import Carrito
from db import _dbi
from constantes import *

class Ecommerce():
  def __init__(self) -> None:                                                                 # * * * Constructor * * *
      self.__usuario = Usuario()
      self.__ui = UI()
      self.__validador = Validador()
      self.__carrito = Carrito()


  def __ver_comprar_productos(self):
    while True:                                                                               # * * * Mostrar Productos * * *
      self.__ui.view.titulo_menu(self.__ui.view.get_menu()["invitado"][0] if (self.__usuario.get_id() == 0) else self.__ui.view.get_menu()["usuario"][1])
      _productos = _dbi.get_fetchall("get_productos")
      self.__ui.view.listar_productos(_productos)
      self.__ui.view.mostrar_mensajes(self.__validador.get_mensajes())
      if (self.__usuario.get_id() == 0):                                                      # Invitado, esperar tecla y Volver
        self.__ui.enter_para_continuar()
        break

      str_opcion = "Ingrese el Num. del Producto que desea Comprar (0 para Volver): "
      opcion_menu = self.__validador.get_opcion_menu(self.__ui.get_opcion_input(str_opcion), len(_productos))
      if (opcion_menu == 0):                                                                  # Volver
        break
      elif (len(self.__validador.get_errores()) == 0):
        cantidad = self.__validador.get_opcion_menu(self.__ui.get_opcion_input("Ingrese la Cantidad (5 Max., 0 para Cancelar): "), 5, "Cantidad Incorrecta")
        if ((cantidad > 0) and (len(self.__validador.get_errores()) == 0)):                   # * * * COMPRAR PRODUCTO segun Cantidad seleccionada * * *
          _producto = _productos[opcion_menu-1]
          descripcion = _producto[P_MARCA] + ' ' + _producto[P_DESCRIPCION]
          self.__carrito.registrar_compra([_producto[P_ID_PRODUCTO], cantidad, _producto[P_PRECIO], descripcion])
          self.__validador.set_mensaje(f"Se agregó a su Carrito, {cantidad} x {descripcion} por el valor de {cantidad * _producto[P_PRECIO]}")


  def __ver_carrito(self):
    while True:
      self.__ui.view.titulo_menu(self.__ui.view.get_menu()["usuario"][0])
      _compras = self.__carrito.get_compras()
      if (len(_compras) > 0):                                                                 # * * * * * * Carrito CON Compras * * * * * *
        self.__ui.view.listar_compras(_compras, self.__carrito.get_total())
        self.__ui.view.mostrar_mensajes(self.__validador.get_mensajes())
        str_opcion = "Ingrese el Num. de la Compra que desea Eliminar del Carrito (0 para Volver): "
        opcion_menu = self.__validador.get_opcion_menu(self.__ui.get_opcion_input(str_opcion), len(_compras) + 1)
        opcion_finalizar_compra = len(_compras) + 1
        if (opcion_menu == 0):                                                                # * * * * * * Volver * * * * * *
          break
        elif (len(self.__validador.get_errores()) == 0):
          if (opcion_menu == opcion_finalizar_compra):
            if (self.__validador.b_pregunta(self.__ui.get_respuesta("Finalizar la Compra"))): # * * * * * * finalizar Compra * * * * * *
              total_carrito = self.__carrito.get_total()
              if (self.__carrito.is_finalizar_compra()):
                self.__validador.set_mensaje(f"Su Compra por un Total de {total_carrito} fué finalizada correctamente")
                break
          else:                                                                               # * * * * * * Borrar Compra * * * * * *
            _compra = _compras[opcion_menu-1]
            str_pregunta = f"eliminar del carrito, la compra {_compra[C_CANTIDAD]} x {_compra[C_PRECIO]} de {_compra[C_DESCRIPCION]}"
            if (self.__validador.b_pregunta(self.__ui.get_respuesta(str_pregunta))):
              self.__carrito.borrar_compra(_compra)
              self.__validador.set_mensaje(f"Se eliminó correctamente, la compra {_compra[C_CANTIDAD]} x {_compra[C_PRECIO]} de {_compra[C_DESCRIPCION]}")
      else:                                                                                   # * * * * * * Carrito Vacio * * * * * *
        print("\nCarrito de Compras Vacio.")
        self.__ui.view.mostrar_mensajes(self.__validador.get_mensajes())
        self.__ui.enter_para_continuar()
        break


  def __login_usuario(self):
    while True:
      self.__ui.view.titulo_menu("Login")
      _login_usuario = self.__validador.get_login(self.__usuario, self.__ui.get_login_usuario())
      if (_login_usuario == None):                                                            # * * * LOGIN Incorrecto * * *
        self.__ui.view.mostrar_mensajes(self.__validador.get_mensajes())
        if (self.__ui.is_volver()):                                                           # * * * Volver * * *
          break
      else:                                                                                   # * * * LOGIN Correcto * * *
        self.__usuario.set_login(_login_usuario)
        self.__carrito.set_pendiente(self.__usuario.get_id())
        break


  def __registro_usuario(self):                                                               # * * * REGISTRO de Usuario * * *
    while True:
      self.__ui.view.titulo_menu("Registro de Usuario")
      _reg_usuario = self.__validador.registro_usuario(self.__usuario, self.__ui.get_registro_usuario())
      if (_reg_usuario == None):
        self.__ui.view.mostrar_mensajes(self.__validador.get_mensajes())
        if (self.__ui.is_volver()):
          break
      else:
        break


  def __logout(self):                                                                         # * * * LOGOUT * * *
    self.__usuario.logout()
    self.__carrito.vaciar()


  def __mostrar_vista(self, perfil_usuario:str, ind_menu:int, _registros:list=[]):            # * * * Mostrar Vista segun Perfil del Usuario y la Opcion elegida * * *
    self.__ui.view.titulo_menu(self.__ui.view.get_menu()[perfil_usuario][ind_menu])
    if (perfil_usuario == PF_ADMIN):
      if (ind_menu in [0, 1]):
        self.__ui.view.listado_generico(_registros)
      elif (ind_menu == 2):
        self.__ui.view.listar_productos(_dbi.get_fetchall("get_productos"), IS_ADMIN)
      elif (ind_menu == 3):
        self.__ui.view.listar_usuarios(_dbi.get_fetchall("get_usuarios"))
      elif (ind_menu == 4):
        self.__ui.view.resumen_carritos(_dbi.get_fetchall("get_resumen_carritos"))
    elif (perfil_usuario == PF_USUARIO):
      if (ind_menu == 2):
        self.__ui.view.mostrar_datos_usuario(self.__usuario, self.__carrito.get_carritos_usuario(self.__usuario.get_id()))
    self.__ui.enter_para_continuar()


  def __set_login(self): # solo para desarrollo
    # self.__usuario.set_login([1, 12345678, "Admin", 1, "admin@email.com", "", 1, "CABA", "Buenos Aires", "Argentina"])
    self.__usuario.set_login([2, 22354687, "Enzo", 1, "enzo@gmail.com", "", 0, "CABA", "Buenos Aires", "Argentina"])
    self.__carrito.set_pendiente(self.__usuario.get_id())


  def menu_principal(self):
    # self.__set_login() # solo para desarrollo
    while True:
      _perfil_menu_usuario = [PF_INVITADO, ""]                                                # * * * Definir Perfil del Usuario * * *
      if (self.__usuario.is_logueado()):
        _perfil_menu_usuario = [PF_USUARIO, f"   {self.__usuario.get_nombre()} (Usuario)"]
      if (self.__usuario.is_admin()):
        _perfil_menu_usuario = [PF_ADMIN, f"   {self.__usuario.get_nombre()} (Admin)"]

      self.__ui.view.menu_principal(_perfil_menu_usuario, self.__validador.get_mensajes())    # * * * Mostrar Menu y Obtener opcion ingesada * * *
      opcion_menu = self.__validador.get_opcion_menu(self.__ui.get_opcion_input(), self.__ui.view.get_cant_opciones())

      if (self.__usuario.is_admin()):                                                         # * * * Admin * * *
        if (opcion_menu == 1):
          self.__mostrar_vista(PF_ADMIN, opcion_menu-1, _dbi.get_fetchall("get_categorias"))
        elif (opcion_menu == 2):
          self.__mostrar_vista(PF_ADMIN, opcion_menu-1, _dbi.get_fetchall("get_marcas"))
        elif (opcion_menu in [3, 4, 5]):
          self.__mostrar_vista(PF_ADMIN, opcion_menu-1)
        elif (opcion_menu == 6):
          self.__logout()
      elif (self.__usuario.is_logueado()):                                                    # * * * Usuario logueado * * *
        if (opcion_menu == 1):
          self.__ver_carrito()
        elif (opcion_menu == 2):
          self.__ver_comprar_productos()
        elif (opcion_menu == 3):
          self.__mostrar_vista(PF_USUARIO, opcion_menu-1)
        elif (opcion_menu == 4):
          self.__logout()
      else:                                                                                   # * * * Guest * * *
        if (opcion_menu == 1):
          self.__ver_comprar_productos()
        if (opcion_menu == 2):
          self.__login_usuario()
        elif (opcion_menu == 3):
          self.__registro_usuario()

      if (opcion_menu == 0):                                                                  # * * * Salir * * *
        break
