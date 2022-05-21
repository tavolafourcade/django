from django.contrib import admin
from django.urls import path
from Proyecto_temp.views import saludo
from Proyecto_temp.views import segunda_vista
from Proyecto_temp.views import diaDeHoy
from Proyecto_temp.views import miNombreEs
from Proyecto_temp.views import edad


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('segunda_vista/', segunda_vista),
    path('diaDeHoy/', diaDeHoy),
    path('miNombreEs/<nombre>',miNombreEs),
    path('miEdadEs/<year>',edad
    )

]
