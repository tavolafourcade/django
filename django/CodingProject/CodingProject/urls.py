from django.contrib import admin
from django.urls import path
from CodingApp.views import course

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', course)
]
