from django.contrib import admin
from django.urls import path
from api.views import listar_dados

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clientes/', listar_dados),
]
