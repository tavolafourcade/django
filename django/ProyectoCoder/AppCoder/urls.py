from django.urls import path
from AppCoder.views import profesores, curso, inicio, cursos, estudiantes, entregables
# from AppCoder.views import curso, profesores

urlpatterns = [
  path('curso/', curso),
  path('profesores/', profesores, name='Profesores'),
  path('cursos/', cursos, name='Cursos'),
  path('estudiantes/', estudiantes, name='Estudiantes'),
  path('entregables/', entregables, name='Entregables'),
  path('inicio/', inicio, name='Inicio'),
]