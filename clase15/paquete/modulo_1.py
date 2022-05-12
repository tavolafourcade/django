class Persona:

  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido


  def __str__(self):
    return "NOMBRE {} APELLIDO {}".format(self.nombre, self.apellido)

#OJO esto es el primer ejemplo, siempre es aconsejable que los 
#modulos y paquetes tengan nombres representativos