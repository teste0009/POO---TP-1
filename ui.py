from view import View

class UI(): # Interface de Usuario
  def __init__(self) -> None:
    self.view = View()

  def get_opcion_input(self, texto:str = "Ingrese una opción: ") -> int:
    try:
      opcion_input = int(input(texto))
    except:
      opcion_input = -1
    return opcion_input

  def get_input_login(self) -> list:
    return [input("Ingrese su email: "), input("Ingrese su password: ")]

  def get_input_registro(self) -> list:
    return [input("Ingrese su DNI: "), input("Ingrese su Nombre: "), input("Ingrese su Email: "), input("Ingrese su Password: "),
      input("Reingrese su Password: "), input("Ingrese el Pais: "), input("Ingrese la Provincia: "), input("Ingrese su Ciudad: "), ]

  def get_volver_o_reintentar(self) -> bool:
    return True if (input("Presione una tecla para reintentar (0 para Volver) ") == "0") else False

  def enter_para_continuar(self):
    input("Presione 'Enter' para continuar: ")

  def get_respuesta(self, pregunta:str) -> str:
    print()
    return input(f"Esta seguro de {pregunta}? (S/N) ")
