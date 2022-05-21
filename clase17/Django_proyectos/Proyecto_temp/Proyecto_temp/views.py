from django.http import HttpResponse
import datetime

def saludo(request):
  return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
  return HttpResponse("<br><br>Ya entendimos")

def diaDeHoy(request):
  dia = datetime.datetime.now()
  texto = 'Hoy es : {}'.format(dia)
  return HttpResponse(texto)

def miNombreEs(self, nombre):
  documentoDeTexto = "Mi nombre es: <br><br> {}".format(nombre)

  return HttpResponse(documentoDeTexto)

def edad(self, anio):
  currentDateTime = datetime.datetime.now()
  date = currentDateTime.date()
  year = date.strftime("%Y")
  edad = int(anio) - year
  documentoDeTexto = "Mi edad es: <br><br> {}".format(edad)

  return HttpResponse(documentoDeTexto)