from validate_email import validate_email
from usuario import Usuario
from db import _dbi
from constantes import *


class Validador():
  def __init__(self) -> None:
      self.__mensajes = {"ERROR": [], "Mensaje": [], "debug": [],}

  def set_mensaje(self, mensaje:str) -> None:
    self.__mensajes["Mensaje"].append(mensaje)

  def set_error(self, error:str) -> None:
    self.__mensajes["ERROR"].append(error)

  def set_debug(self, debug:str) -> None:
    self.__mensajes["debug"].append(debug)

  def get_mensajes(self) -> dict:
    _mensajes = self.__mensajes
    self.__mensajes = {"ERROR": [], "Mensaje": [], "debug": [],}
    return _mensajes

  def get_errores(self) -> list:
    return self.__mensajes["ERROR"]

  def b_pregunta(self, respuesta:str) -> bool:
    _si = ["s", "si"]
    _no = ["n", "no"]
    if (respuesta.lower() in _si):
      return True
    elif (respuesta.lower() in _no):
      return False
    else:
      self.set_error("Respuesta Incorrecta")
      return False

  def get_opcion_menu(self, opcion_input:int, cant_opciones:int, str_error:str = "Opción incorrecta") -> int:
    if (opcion_input >= 0 and opcion_input <= cant_opciones):
      return opcion_input
    else:
      self.set_error(str_error)
      return -1

  def get_login(self, _usuario:Usuario, _login:list):
    _get_login = _usuario.get_login(_login)
    if (_get_login == None):
      self.set_error("Email o Password, incorrecto")
    else:
      self.set_mensaje("Login Correcto")
    return _get_login

  def registro_usuario(self, _usuario:Usuario, _registro:list):
    for i in range(len(_registro)):
      _registro[i] = _registro[i].strip()

    try:
      dni = int(_registro[R_DNI])
    except:
      self.set_error("DNI Incorrecto")

    if (_registro[R_NOMBRE] == ""):
      self.set_error("Nombre vacio")

    if (_registro[R_EMAIL] == ""):
      self.set_error("Email vacio")
    elif (validate_email(_registro[R_EMAIL]) == False):
      self.set_error("Email incorrecto")
    elif (_usuario.is_existe_email(_registro[R_EMAIL])):
      self.set_error("Email ya registrado")

    _caracteres_especiales=['_', '-', '$','@','#','%']
    if (_registro[R_PASSWORD] == ""):
      self.set_error('Password vacio')
    elif (len(_registro[R_PASSWORD]) < 6):
      self.set_error("El Password debe contener al menos 6 caracteres")
    elif (not any(i.islower() for i in _registro[R_PASSWORD])):
      self.set_error("El Password debe contener al menos una letra minuscula")
    elif (not any(i.isupper() for i in _registro[R_PASSWORD])):
      self.set_error("El Password debe contener al menos una letra mayuscula")
    elif (not any(i.isdigit() for i in _registro[R_PASSWORD])):
      self.set_error("El Password debe contener al menos un caracter numeral")
    elif (not any(i in _caracteres_especiales for i in _registro[R_PASSWORD])):
      self.set_error("El Password debe contener al menos uno de los carateres especiales " + ' '.join(_caracteres_especiales))
    elif (_registro[R_PASSWORD] != _registro[R_PASSWORD_RI]):
      self.set_error("El Password Reingresado es diferente")

    if (_registro[R_PAIS] == ""):
      self.set_error("Campo Pais vacio")
    else:
      id_pais = _dbi.get_id("id_pais", (_registro[R_PAIS],))
      if (id_pais == 0):
        self.set_error("Pais Incorrecto")
      elif (_registro[R_PROVINCIA] == ""):
        self.set_error("Campo Provincia vacio")
      else:
        id_provincia = _dbi.get_id("id_provincia", (_registro[R_PROVINCIA], id_pais))
        if (id_provincia == 0):
          self.set_error("Provincia Incorrecta")
        elif (_registro[R_CIUDAD] == ""):
          self.set_error("Campo Ciudad vacio")
        else:
          id_ciudad = _dbi.get_id("id_ciudad", (_registro[R_CIUDAD], id_provincia))
          if (id_ciudad == 0):
            self.set_error("Ciudad Incorrecta")

    if (len(self.get_errores()) > 0):
      return None
    else:
      _usuario.registrar((_registro[R_DNI], _registro[R_NOMBRE], id_ciudad, _registro[R_EMAIL], _dbi.encode_pass(_registro[R_PASSWORD])))
      self.set_mensaje("Registro de Nuevo Usuario Correcto")
      return _registro
