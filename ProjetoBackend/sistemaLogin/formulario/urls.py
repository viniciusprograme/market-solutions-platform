from django.urls import path
from .views import login_view, logout_view, home_view, registro_view

urlpatterns = [
    path('', home_view, name='home'), # Para ser enviada mo inicio para a /home/
    path('login/', login_view, name='login'), # Rota para Login
    path('logout/', logout_view, name='logout'), # Rota para Logout
    path('home/', home_view, name='home'), # Rota para Home
    path('registro/', registro_view, name='registro'), # Rota para Registro
]

# Rotas de URLs da aplicação formulario para o projeto sistemaLogin