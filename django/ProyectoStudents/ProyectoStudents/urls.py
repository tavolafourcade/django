from django.contrib import admin
from django.urls import path
from AppCoderhouse.views import curso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('curso/', curso),
]
