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

def profesores(self):
  documento = f"Página de profesores"
  return HttpResponse(documento)

def cursos(self):
  documento = f"Página de cursos"
  return HttpResponse(documento)

def estudiantes(self):
  documento = f"Página de estudiantes"
  return HttpResponse(documento)

def entregables(self):
  documento = f"Página de entregables"
  return HttpResponse(documento)

def mi_plantilla(self):
  plantilla = loader.get_template('plantilla.html')
  documento = plantilla.render()
  return HttpResponse(documento)