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
  return render(request, 'appCoder/profesores.html')

def cursos(request):
  return render(request, 'appCoder/cursos.html')


def estudiantes(self):
  documento = f"Página de estudiantes"
  return HttpResponse(documento)

def entregables(self):
  documento = f"Página de entregables"
  return HttpResponse(documento)

def inicio(self):
  plantilla = loader.get_template('AppCoder/inicio.html')
  documento = plantilla.render()
  return HttpResponse(documento)
