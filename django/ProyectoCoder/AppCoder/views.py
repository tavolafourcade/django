from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.template import loader
# Create your views here.

def curso(self):
  curso = Curso(nombre="Desarrollo backend", camada=18340)
  curso.save()
  documento = f"Curso: {curso.nombre} - Camada: {curso.camada}"
  return HttpResponse(documento)

def profesores(request):
  return render(request, 'profesores.html')

def cursos(request):
  return render(request, 'cursos.html')

def estudiantes(request):
  return render(request, 'estudiantes.html')

def entregables(request):
  return render(request, 'entregables.html')

def mi_plantilla(self):
  plantilla = loader.get_template('plantilla.html')
  documento = plantilla.render()
  return HttpResponse(documento)