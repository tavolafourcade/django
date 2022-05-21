from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
import datetime

def saludo(request):
  return HttpResponse("Hola mundo")

def segunda_vista(request):
  return HttpResponse("Segunda vista")

def DiaDeHoy(request):
  dia = datetime.datetime.now()
  texto = 'Hoy es: {}'.format(dia)
  return HttpResponse(texto)

def nombre_persona(self, nombre):
  resultado = "Mi nombre es: <br> <br> {}".format(nombre)
  return HttpResponse(resultado)

def primera_template(self):

  nombre = 'Milagros'
  apellido = 'Garcia'
  lista_notas = [2,4,5,6,8]

  diccionario = {"nombre": nombre, "apellido": apellido, "creation_date": datetime.datetime.now(), "lista_notas": lista_notas}

  # html = open('/Users/octaviolafourcade/Documents/PYTHON/django/Proyecto1/Proyecto1/plantillas/template1.html')
  # plantilla = Template(html.read()) #Se carga en memoria nuestro documento, template1   
  #   ##OJO importar template y contex, con: from django.template import Template, Context

  # html.close() #cerramos el archivo

  # miContexto = Context(diccionario) #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

  plantilla = loader.get_template('template1.html')
  documento = plantilla.render(diccionario) #Aca renderizamos la plantilla en documento

  return HttpResponse(documento)