from django.http import HttpResponse
from django.shortcuts import render

from AppCoderhouse.models import Curso

def curso(self):
  curso = Curso(nombre="Desarrollo Web", camada="25644")
  curso.save()
  documento_texto = f'---> Curso: {curso.nombre} Camada: {curso.camada}'
  return HttpResponse(documento_texto)