from django.urls import path
from AppCoder import views

urlpatterns = [
  path('curso/', views.curso),
  path('profesores/', views.profesores),

]
