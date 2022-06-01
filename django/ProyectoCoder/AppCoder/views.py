from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.template import loader
from AppCoder.forms import CursosFormulario
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
    miFormulario = CursosFormulario(request.POST)
    
    if miFormulario.is_valid():
      informacion = miFormulario.cleaned_data # Esto me trae los datos limpios
      curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
      curso.save()
      return render(request, 'AppCoder/inicio.html')
    
  else:
    miFormulario = CursosFormulario() #Creo mi formulario vacío
  return render(request, 'AppCoder/cursosFormulario.html', {'miFormulario':miFormulario})

def inicio(self):
  plantilla = loader.get_template('AppCoder/inicio.html')
  documento = plantilla.render()
  return HttpResponse(documento)

def busquedaComision(request):
  return render(request, 'AppCoder/busquedaComision.html')

def buscar(request):
  respuesta = f"Estoy buscando la comision {request.GET['camada']}"
  return HttpResponse(respuesta)