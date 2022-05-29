from django.urls import path
from AppCoder.views import profesores, curso, cursos, estudiantes, entregables, mi_plantilla
from AppCoder.views import mi_plantilla
# from AppCoder.views import curso, profesores

urlpatterns = [
  path('curso/', curso),
  path('profesores/', profesores),
  path('cursos/', cursos),
  path('estudiantes/', estudiantes),
  path('entregables/', entregables),
  path('mi_plantilla/', mi_plantilla),
]