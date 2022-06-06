from django.urls import path
from AppCoder.views import inicio, profesores, curso, cursos, estudiantes, entregables, cursosFormulario, busquedaComision, buscar, leerProfesores
# from AppCoder.views import curso, profesores

urlpatterns = [
  path('curso/', curso),
  path('profesores/', leerProfesores, name='profesores'),
  path('cursos/', cursos, name='cursos'),
  path('estudiantes/', estudiantes, name='estudiantes'),
  path('entregables/', entregables, name='entregables'),
  path('inicio/', inicio, name='inicio'),
  path('cursosFormulario/', cursosFormulario, name='cursosFormulario'),
  path('busquedaComision/', busquedaComision, name='busquedaComision'),
  path('buscar/', buscar, name='buscar'),
]