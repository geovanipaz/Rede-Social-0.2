 
from django.urls import path
from app_login import views

app_name = 'app_login'

urlpatterns = [
    path('', views.index, name='index'),
    path('criausuario/', views.criaUsuario, name='cadastrar'),
    path('login/', views.login, name='login'),
    path('perfil/<username>/', views.perfil, name='perfil'),
    path('editarperfil/', views.editarperfil, name='editarperfil'),
    path('logout/',views.logout_usuario, name='logout'),
    path('seguir/<username>/', views.seguir, name='seguir'),
    path('deseguir/<username>/', views.deseguir, name='deseguir'),
    path('feed/', views.feed, name='feed'),
    
]
