from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso, Profesor, Estudiante
from django.template import loader
from AppCoder.forms import CursoFormulario, ProfesorFormulario, UserRegistrationForm, UserEditForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# LOGIN
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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

def cursoFormulario(request):
  if request.method == 'POST':
    miFormulario = CursoFormulario(request.POST)
    if miFormulario.is_valid():
      informacion = miFormulario.cleaned_data
    nombre = informacion['curso']
    camada = informacion['camada']
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    return render(request, 'AppCoder/inicio.html')
  else:
    miFormulario = CursoFormulario()
  return render(request, 'appCoder/cursoFormulario.html', {'miFormulario':miFormulario})



def busquedaCamada(request):
  return render(request, 'appCoder/busquedaCamada.html')

def buscar(request):
  # respuesta = f"Estoy buscando la comisión {request.GET['camada']}"
  if request.GET['camada']:
    camada = request.GET['camada']
    cursos = Curso.objects.filter(camada=camada)
    return render(request, 'appCoder/resultadosBusqueda.html', {'cursos':cursos, 'camada':camada})
  else:
    respuesta = "No se ha ingresado ninguna comisión" 
  return HttpResponse(respuesta)

# CRUD Read
def leerProfesores(request):
  profesores = Profesor.objects.all()
  contexto = {'profesores':profesores}
  return render(request, 'appCoder/profesores.html', {'profesores':profesores})

# CRUD Create

def profesorFormulario(request):
  if request.method == 'POST':
    miFormulario = ProfesorFormulario(request.POST)
    if miFormulario.is_valid():
      informacion = miFormulario.cleaned_data
    nombre = informacion['nombre']
    apellido = informacion['apellido']
    email = informacion['email']
    profesion = informacion['profesion']

    profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
    profesor.save()
    return render(request, 'AppCoder/inicio.html')
  else:
    miFormulario = ProfesorFormulario()
  return render(request, 'appCoder/profesorFormulario.html', {'miFormulario':miFormulario})

# CRUD Delete
@login_required
def eliminarProfesor(request, nombre):
  profesor = Profesor.objects.get(nombre=nombre)
  profesor.delete()

  profesores = Profesor.objects.all()
  contexto = {'profesores':profesores}
  return render(request, 'appCoder/profesores.html', contexto)

@login_required
def editarProfesor(request, profesor_nombre):
  profesor = Profesor.objects.get(nombre=profesor_nombre)
  if request.method == 'POST':
    miFormulario = ProfesorFormulario(request.POST)
    if miFormulario.is_valid():
      informacion = miFormulario.cleaned_data
      profesor.nombre = informacion['nombre']
      profesor.apellido = informacion['apellido']
      profesor.email = informacion['email']
      profesor.profesion = informacion['profesion']
      profesor.save()

      profesores = Profesor.objects.all()
      contexto = {'profesores':profesores}
      return render(request, 'appCoder/profesores.html', contexto)
  else:
    miFormulario = ProfesorFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido, 'email':profesor.email, 'profesion':profesor.profesion}) 
    contexto = {'miFormulario':miFormulario, 'profesor_nombre':profesor_nombre}
    return render(request, 'appCoder/editarProfesor.html', contexto)

#---------------------------------------------------------------------------------------------------------------------
# LISTVIEW
class EstudiantesList(LoginRequiredMixin, ListView):
  model = Estudiante
  template_name = 'AppCoder/estudiante_list.html'

# DETAILVIEW
class EstudianteDetalle(DetailView):
  model = Estudiante
  template_name = 'AppCoder/estudiante_detalle.html'

class EstudianteCreacion(CreateView):
  model = Estudiante
  success_url = reverse_lazy('estudiante_listar')
  fields = ['nombre','apellido','email']

class EstudianteEdicion(UpdateView):
  model = Estudiante
  success_url = reverse_lazy('estudiante_listar')
  fields = ['nombre','apellido','email']

class EstudianteEliminacion(DeleteView):
  model = Estudiante
  success_url = reverse_lazy('estudiante_listar')

#---------------------------------------------------------------------------------------------------------------------
# LOGIN
def login_request(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      usuario = form.cleaned_data.get('username')
      clave = form.cleaned_data.get('password')
      # Autenticación de usuario
      user = authenticate(username=usuario, password=clave) # Si este usuario existe me lo trae
      if user is not None:
        login(request,user) # Si existe, lo loguea
        return render(request, 'AppCoder/inicio.html', {'mensaje': f'Bienvenido {usuario}'})
      else:
        return render(request, 'AppCoder/inicio.html', {'mensaje': 'Error, datos incorrectos'})
    else:
      return render(request,'AppCoder/inicio.html', {'mensaje': 'Error, formulario erróneo'})
  form = AuthenticationForm() # Creo un formulario vacío si vengo por GET
  return render(request, 'AppCoder/login.html', {'form':form}) 

# REGISTER
def register_request(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      form.save()
      return render(request, 'AppCoder/inicio.html', {'mensaje': f'Usuario {username} creado'})
    else:
      return render(request, 'AppCoder/inicio.html', {'mensaje': 'Error, no se pudo crear el usuario'})
  else:
    form = UserRegistrationForm()
    return render(request, 'AppCoder/register.html', {'form':form})

@login_required
def editarPerfil(request):
  # Viene del modelo de Django para usuarios
  usuario = request.user

  if request.method == 'POST':
    formulario = UserEditForm(request.POST, instance=usuario)
    if formulario.is_valid():
      informacion = formulario.cleaned_data
      usuario.email = informacion['email']
      usuario.password1 = informacion['password1']
      usuario.password2 = informacion['password2']
      usuario.save()
      return render(request, 'AppCoder/inicio.html', {'mensaje': 'Datos cambiado exitosamente'})
  else:
    formulario = UserEditForm(instance=usuario)
  return render(request, 'AppCoder/editarPerfil.html', {'formulario':formulario, 'usuario':usuario.username})