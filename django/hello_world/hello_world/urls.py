from django.contrib import admin
from django.urls import path
from hello_world.views import first_template

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_template/', first_template),
]
