from ui import UI # Interface de Usuario
from validador import Validador
from usuario import Usuario
from carrito import Carrito
from db import _dbi

class Ecommerce():
  def __init__(self) -> None:
      self.__usuario = Usuario()
      self.__ui = UI()
      self.__validador = Validador()
      self.__carrito = Carrito()

  def __ver_comprar_productos(self):
    while True:
      self.__ui.view.menu_generico(self.__ui.view.get_menu()["logueado"][1])
      _productos = _dbi.get_fetchall("get_productos")
      self.__ui.view.listar_productos(_productos)
      self.__ui.view.mostrar_mensajes(self.__validador.get_mensajes())
      str_opcion = "Ingrese el Num. del Producto que desea Comprar (0 para Volver): "
      opcion = self.__validador.get_opcion_menu(self.__ui.get_opcion_input(str_opcion), len(_productos))
      if (opcion == 0): # Volver
        break
      elif (len(self.__validador.get_errores()) == 0):
        cantidad = self.__validador.get_opcion_menu(self.__ui.get_opcion_input("Ingrese la Cantidad (5 Max., 0 para Cancelar): "), 5, "Cantidad Incorrecta")
        if ((cantidad > 0) and (len(self.__validador.get_errores()) == 0)): # Comprar
          _producto = _productos[opcion-1]
          descripcion = _producto[2] + ' ' + _producto[3] # marca + ' ' + descripcion
          _compra = [_producto[0], cantidad, _producto[4], descripcion] # id_producto, cantidad, precio
          self.__carrito.registrar_compra(_compra)
          self.__validador.set_mensaje(f"Se agregó a su Carrito, {cantidad} x {descripcion} por el valor de {cantidad * _producto[4]}")

  def __ver_carrito(self):
    while True:
      self.__ui.view.menu_generico(self.__ui.view.get_menu()["logueado"][0])
      _compras = self.__carrito.get_compras()
      if (len(_compras) > 0):
        self.__ui.view.listar_compras(_compras, self.__carrito.get_total())
        self.__ui.view.mostrar_mensajes(self.__validador.get_mensajes())
        str_opcion = "Ingrese el Num. de la Compra que desea Eliminar del Carrito (0 para Volver): "
        opcion = self.__validador.get_opcion_menu(self.__ui.get_opcion_input(str_opcion), len(_compras) + 1)
        opcion_finalizar_compra = len(_compras) + 1
        if (opcion == 0): # * * * * * * Volver * * * * * *
          break
        elif (len(self.__validador.get_errores()) == 0):
          if (opcion == opcion_finalizar_compra):
            if (self.__validador.b_pregunta(self.__ui.get_respuesta("Finalizar la Compra"))): # * * * * * * finalizar Compra * * * * * *
              total_carrito = self.__carrito.get_total()
              if (self.__carrito.b_finalizar_compra()):
                self.__validador.set_mensaje(f"Su Compra por un Total de {total_carrito} fué finalizada correctamente")
                break
          else: # * * * * * * Borrar Compra * * * * * *
            _compra = _compras[opcion-1]
            str_pregunta = f"eliminar del carrito, la compra {_compra[1]} x {_compra[2]} de {_compra[3]}"
            if (self.__validador.b_pregunta(self.__ui.get_respuesta(str_pregunta))):
              self.__carrito.borrar_compra(_compra)
              self.__validador.set_mensaje(f"Se eliminó correctamente, la compra {_compra[1]} x {_compra[2]} de {_compra[3]}")
      else: # * * * * * * Carrito Vacio * * * * * *
        print("\nCarrito de Compras Vacio.")
        self.__ui.view.mostrar_mensajes(self.__validador.get_mensajes())
        self.__ui.enter_para_continuar()
        break

  def __set_login_usuario(self):
    while True:
      self.__ui.view.menu_generico("Login")
      _login_usuario = self.__validador.get_login(self.__usuario, self.__ui.get_input_login())
      if (_login_usuario == None):
        self.__ui.view.mostrar_mensajes(self.__validador.get_mensajes())
        if (self.__ui.get_volver_o_reintentar()):
          break
      else:
        self.__usuario.set_login(_login_usuario)
        self.__carrito.set_pendiente(self.__usuario.get_id())
        break

  def __set_registro_usuario(self):
    while True:
      self.__ui.view.menu_generico("Registro de Usuario")
      _reg_usuario = self.__validador.registro_usuario(self.__usuario, self.__ui.get_input_registro())
      if (_reg_usuario == None):
        self.__ui.view.mostrar_mensajes(self.__validador.get_mensajes())
        if (self.__ui.get_volver_o_reintentar()):
          break
      else:
        break

  def __ver_mis_datos(self):
    self.__ui.view.menu_generico(self.__ui.view.get_menu()["logueado"][2])
    self.__ui.view.mostrar_datos(self.__usuario, self.__carrito.get_carritos_usuario(self.__usuario.get_id()))
    self.__ui.enter_para_continuar()

  def __set_logout(self):
    self.__usuario.set_logout()
    self.__carrito.reiniciar()

  def __listar_registros(self, ind_menu:int, _registros:list):
    self.__ui.view.menu_generico(self.__ui.view.get_menu()["admin"][ind_menu])
    self.__ui.view.listar_registros(_registros)
    self.__ui.enter_para_continuar()

  def __listar_productos(self):
    self.__ui.view.menu_generico(self.__ui.view.get_menu()["admin"][2])
    self.__ui.view.listar_productos(_dbi.get_fetchall("get_productos"), True)
    self.__ui.enter_para_continuar()

  def __listar_usuarios(self):
    self.__ui.view.menu_generico(self.__ui.view.get_menu()["admin"][3])
    self.__ui.view.listar_usuarios(_dbi.get_fetchall("get_usuarios"))
    self.__ui.enter_para_continuar()

  def __resumen_carritos(self):
    self.__ui.view.menu_generico(self.__ui.view.get_menu()["admin"][4])
    self.__ui.view.resumen_carritos(_dbi.get_fetchall("get_resumen_carritos"))
    self.__ui.enter_para_continuar()

  def __set_login(self): # solo para desarrollo
    # self.__usuario.set_login([1, 12345678, "Admin", 1, "admin@email.com", "", 1, "CABA", "Buenos Aires", "Argentina"])
    self.__usuario.set_login([2, 22354687, "Enzo", 1, "enzo@gmail.com", "", 0, "CABA", "Buenos Aires", "Argentina"])
    self.__carrito.set_pendiente(self.__usuario.get_id())

  def menu_principal(self):
    # self.__set_login() # solo para desarrollo
    while True:
      _tipo_menu_usuario = ["default", ""]
      if (self.__usuario.is_admin()):
        _tipo_menu_usuario = ["admin", f"{self.__usuario.get_nombre()} (Admin)"]
      if (self.__usuario.is_logueado()):
        _tipo_menu_usuario = ["logueado", f"{self.__usuario.get_nombre()} (Usuario)"]

      self.__ui.view.menu_principal(_tipo_menu_usuario, self.__validador.get_mensajes())
      opcion = self.__validador.get_opcion_menu(self.__ui.get_opcion_input(), self.__ui.view.get_cant_opciones())

      if (self.__usuario.is_admin()): # * * * Admin * * *
        if (opcion == 1):
          self.__listar_registros(opcion-1, _dbi.get_fetchall("get_categorias"))
        elif (opcion == 2):
          self.__listar_registros(opcion-1, _dbi.get_fetchall("get_marcas"))
        elif (opcion == 3):
          self.__listar_productos()
        elif (opcion == 4):
          self.__listar_usuarios()
        elif (opcion == 5):
          self.__resumen_carritos()
        elif (opcion == 6):
          self.__set_logout()
      elif (self.__usuario.is_logueado()): # * * * Usuario logueado * * *
        if (opcion == 1):
          self.__ver_carrito()
        elif (opcion == 2):
          self.__ver_comprar_productos()
        elif (opcion == 3):
          self.__ver_mis_datos()
        elif (opcion == 4):
          self.__set_logout()
      else: # * * * Guest * * *
        if (opcion == 1):
          self.__set_login_usuario()
        elif (opcion == 2):
          self.__set_registro_usuario()

      if (opcion == 0):
        break
