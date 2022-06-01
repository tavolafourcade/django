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
  return render(request, 'AppCoder/profesores.html')

def cursos(request):
  return render(request, 'AppCoder/cursos.html')

def estudiantes(request):
  return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
  return render(request, 'AppCoder/entregables.html')

def cursosFormulario(request):
  if request.method == 'POST':
    print(request.POST)
    curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
    curso.save()
    return render(request, 'AppCoder/inicio.html')
    # nombre = request.POST.get('curso')
    # camada = request.POST.get('camada')
    # curso = Curso(nombre=nombre, camada=camada)
    # curso.save()
  return render(request, 'AppCoder/cursosFormulario.html')

def inicio(self):
  plantilla = loader.get_template('AppCoder/inicio.html')
  documento = plantilla.render()
  return HttpResponse(documento)