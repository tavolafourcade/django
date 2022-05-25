from django.urls import path
from AppCoder import views
from AppCoder.views import mi_plantilla

urlpatterns = [
  path('curso/', views.curso),
  path('profesores/', views.profesores),
  path('mi_plantilla/', mi_plantilla),

]
