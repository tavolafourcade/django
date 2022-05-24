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

# /Users/octaviolafourcade/Documents/PYTHON/django/Proyecto1/Proyecto1/plantillas/

# 'C:/Users/gherr/Desktop/Gonza/Python/Proyecto1/Proyecto1/Plantillas/template1.html'
def probandoTemplate(self):

  nombre = 'Bruno'
  apellido= 'Arias'
  listaDeNotas = [2, 5, 7, 3]

  diccionario = {"nombre":nombre, "apellido":apellido, "listaDeNotas":listaDeNotas}

  # miHtml = open('template1.html')

  # plantilla = Template(miHtml.read())
  # miHtml.close()

  # miContexto = Context(diccionario)
  plantilla = loader.get_template('template1.html')
  documento = plantilla.render(diccionario)

  return HttpResponse(documento)