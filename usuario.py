from db import _dbi
from constantes import *


class Usuario():
  def __init__(self) -> None:
    self.__id = 0
    self.__dni = 0
    self.__nombre = ""
    self.__email = ""
    self.__is_logueado = False
    self.__b_admin = False
    self.__ciudad = ""
    self.__provincia = ""
    self.__pais = ""

  def get_id(self):
    return self.__id

  def get_dni(self):
    return self.__dni

  def get_nombre(self):
    return self.__nombre

  def get_email(self):
    return self.__email

  def get_ciudad(self):
    return self.__ciudad

  def get_provincia(self):
    return self.__provincia

  def get_pais(self):
    return self.__pais

  def set_login(self, _login_usuario:list):
    self.__id = _login_usuario[0]
    self.__dni = _login_usuario[1]
    self.__nombre = _login_usuario[2]
    self.__email = _login_usuario[4]
    self.__is_logueado = True
    self.__b_admin = _login_usuario[6]==1
    self.__ciudad = _login_usuario[7]
    self.__provincia = _login_usuario[8]
    self.__pais = _login_usuario[9]

  def is_logueado(self) -> bool:
    return self.__is_logueado

  def is_admin(self) -> bool:
    return self.__b_admin

  def is_existe_email(self, email:str) -> bool:
    return (_dbi.get_fetchone("get_email", (email, )) != None)

  def get_login(self, _login:list):
    return _dbi.get_fetchone("get_login", (_login[L_EMAIL], _dbi.encode_pass(_login[L_PASSWORD])))

  def registrar(self, _registro:tuple):
    _dbi.commit("insert_usuario", _registro)

  def logout(self):
    self.__init__()
