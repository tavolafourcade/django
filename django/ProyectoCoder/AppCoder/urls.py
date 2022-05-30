from django.urls import path
from AppCoder.views import inicio, profesores, curso, cursos, estudiantes, entregables
# from AppCoder.views import curso, profesores

urlpatterns = [
  path('curso/', curso),
  path('profesores/', profesores, name='profesores'),
  path('cursos/', cursos, name='cursos'),
  path('estudiantes/', estudiantes, name='estudiantes'),
  path('entregables/', entregables, name='entregables'),
  path('inicio/', inicio, name='inicio'),
]