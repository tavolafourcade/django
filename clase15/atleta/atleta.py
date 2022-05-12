# coding=utf-8

#################### CICLISTA ###############################
class Ciclista: 

  #Constructor, con atributos privados
  def __init__(self, estilo):
    self.__estilo = estilo

  #Metodo de este padre
  def hacerBici(self):
    print("Estoy andando en bici o--to")

  #Como quiero mostrar al objeto
  def __str__(self):
    return "Soy un ciclista del estilo{}".format(self.__estilo)

  #Getter y setter
  def get_estilo(self):
    return self.__estilo

  def set_estilo(self, estilo):
    self.__estilo = estilo

#################### CORREDOR ###############################
class Corredor: 

  #Constructor, con atributos privados
  def __init__(self, metros, tipo):
    self.__metros = metros
    self.__tipo = metros

  #Metodo de este padre
  def correr(self):
    print("Estoy corriendoooo....")

  #Como quiero mostrar al objeto
  def __str__(self):
    return "Soy un corredor de  {} del tipo {}".format(self.__metros, self.__tipo)


  #Getter y setter
  def get_metros(self):
    return self.__metros

  def set_metros(self, metros):
    self.__metros = metros

  def get_tipo(self):
    return self.__tipo

  def set_tipo(self, tipo):
    self.__tipo = tipo


#################### NADADOR ###############################
class Nadador:

  def __init__(self, estilo):
    self.__estilo = estilo


  #Metodo de este padre
  def correr(self):
    print("Nadandooooooo.... \o/")


  #Como quiero mostrar al objeto
  def __str__(self):
    return "Soy un nadador de  {}".format(self.__estilo)


  #Getter y setter
  def get_estilo(self):
    return self.__estilo

  def set_estilo(self, estilo):
    self.__estilo = estilo



#Vamos con la clase Hija que hereda de los tres deportes

class TriAtleta(Nadador, Corredor, Ciclista):

  #Consturctor
  def __init__(self, estiloN, metros, tipo, estiloC, nombreYApellido, edad):

    #super().__init__(estiloN, metros, tipo, estiloC)
    #En las multiples el super no te sirve
    Nadador.__init__(self, estiloN)
    Corredor.__init__(self, metros, tipo)
    Ciclista.__init__(self, estiloC)

    self.__nombreYApellido = nombreYApellido
    self.__edad = edad
  
  def __str__(self):
    return Nadador.__str__(self) +"\n"+ Corredor.__str__(self)  +"\n"+ Ciclista.__str__(self) +"\nSoy Genial" +"\nMi nombre es {} con {} años...".format(self.__nombreYApellido, self.__edad)