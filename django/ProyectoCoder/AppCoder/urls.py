from django.urls import path
from AppCoder.views import profesores, curso, inicio, cursos, estudiantes, entregables, cursoFormulario, profesorFormulario, busquedaCamada, buscar, leerProfesores, eliminarProfesor
# from AppCoder.views import curso, profesores

urlpatterns = [
  path('curso/', curso),
  path('cursos/', cursos, name='Cursos'),
  path('estudiantes/', estudiantes, name='Estudiantes'),
  path('entregables/', entregables, name='Entregables'),
  path('inicio/', inicio, name='Inicio'),
  path('cursoFormulario/', cursoFormulario, name='cursoFormulario'),
  path('profesorFormulario/', profesorFormulario, name='profesorFormulario'),
  path('busquedaCamada/', busquedaCamada, name='busquedaCamada'),
  path('buscar/', buscar, name='buscar'),
  path('profesores/', leerProfesores, name='Profesores'),
  path('eliminarProfesor/<nombre>', eliminarProfesor, name='eliminarProfesor')
]