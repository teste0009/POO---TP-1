from db import _dbi
from constantes import *


class Carrito():
  def __init__(self) -> None:
    self.__id = 0
    self.__id_usuario = 0
    self.__total = 0
    self.__b_comprado = False
    self.__compras = []

  def set_b_comprado(self, b_comprado:bool):
    self.__b_comprado = b_comprado

  def get_total(self) -> float:
    return self.__total

  def get_compras(self) -> list:
    return self.__compras

  def __set_id_total(self, id_carrito:int, total:float):
    self.__id = id_carrito
    self.__total = total

  def set_pendiente(self, id_usuario:int):
    self.__id_usuario = id_usuario
    _db_carrito = _dbi.get_fetchone("get_carrito", (id_usuario,))
    if (_db_carrito != None):
      id_carrito, total = _db_carrito
      self.__set_id_total(id_carrito, total)
      _db_compras = _dbi.get_fetchall("get_compras", (id_carrito,))
      if (_db_compras != None):
        for _compra in _db_compras:
          self.__compras.append(list(_compra))

  def get_total_carrito(self):
    _dbi.commit("update_total_carrito", (self.__id, self.__id))
    return _dbi.get_fetchone("get_total_carrito", (self.__id, ))[0]

  def registrar_compra(self, _compra:list):
    sub_total = _compra[C_CANTIDAD] * _compra[C_PRECIO]
    if (self.__id == 0):
      id_carrito = _dbi.get_lastrowid("insert_carrito", (self.__id_usuario, sub_total))
      self.__set_id_total(id_carrito, sub_total)
    else:
      id_carrito = self.__id
    id_compra = _dbi.get_lastrowid("insert_compra", (id_carrito, _compra[C_ID_PRODUCTO], _compra[C_CANTIDAD], sub_total))
    self.__compras.append([id_compra, _compra[C_CANTIDAD], _compra[C_DESCRIPCION], sub_total])
    self.__total = self.get_total_carrito()

  def borrar_compra(self, _compra:list):
    _dbi.get_rowcount("borrar_compra", (_compra[0], ))
    self.__compras.remove(_compra)
    if (len(self.__compras) == 0):
      if (_dbi.get_rowcount("borrar_carrito", (self.__id, )) > 0):
        self.__id, self.__total, self.__b_comprado = 0, 0, False
    else:
      self.__total = self.get_total_carrito()

  def is_finalizar_compra(self) -> bool:
    if (_dbi.get_rowcount("finalizar_compra", (self.__id, )) > 0):
      self.__id, self.__total, self.__b_comprado, self.__compras = 0, 0, False, []
      return True
    else:
      return False

  def get_carritos_usuario(self, id_usuario:int) -> list:
    _carritos_usuario = [0, 0, 0, 0] # cant_pendientes, total_pendientes, cant_comprados, total_comprados
    for int_comprado, cantidad, total in _dbi.get_fetchall("get_carritos_usuario", (id_usuario, )):
      _carritos_usuario[int_comprado*2] = cantidad
      _carritos_usuario[int_comprado*2+1] = total
    return _carritos_usuario

  def vaciar(self):
    self.__init__()