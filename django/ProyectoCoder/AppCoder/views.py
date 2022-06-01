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
  if request.GET['camada']:
    camada = request.GET['camada']
    # Del modelo Curso filtrame los cursos que tengan como camada la variable camada
    cursos = Curso.objects.filter(camada=camada)
    # Quiero que me renderice cursos y a la vez me mande la lista de los cursos como contexto
    return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos':cursos, 'camada':camada})
  else:
    respuesta = "No se ingresó ninguna comisión"
    return HttpResponse(respuesta)