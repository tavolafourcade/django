from django.contrib import admin
from django.urls import path
from Proyecto1.views import segunda_vista
from Proyecto1.views import DiaDeHoy
from Proyecto1.views import nombre_persona
from Proyecto1.views import probandoTemplate
urlpatterns = [
    path('admin/', admin.site.urls),
    path('segundavista/', segunda_vista),
    path('diaDeHoy/', DiaDeHoy),
    path('nombre_persona/<nombre>/', nombre_persona),
    path('probandoTemplate/', probandoTemplate)
]
