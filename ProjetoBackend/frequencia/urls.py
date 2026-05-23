from django.urls import path
from . import views

urlpatterns = [
    path("frequencias/", views.listar_frequencias, name="listar_frequencias"),
    path("frequencias/novo/", views.registrar_frequencia, name="registrar_frequencia"),
]