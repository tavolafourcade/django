from django.urls import path
from AppCoder.views import profesores, curso
from AppCoder.views import mi_plantilla
# from AppCoder.views import curso, profesores

urlpatterns = [
  path('curso/', curso),
  path('profesores/', profesores),
  path('mi_plantilla/', mi_plantilla),
]