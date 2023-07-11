from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import CadPlanta
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage" ),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('cadastrarespecie/', views.Cad, name="Cadastro de Espécie" ),
    path('cadastrarplanta/', login_required(CadPlanta), name='cadastrar_planta'),
    path('minerios/', views.Cadmin, name="Cadastro de minerio"),
    path('estacao/', views.Cadest, name="Cadastro de estacao"),
    path('ph/', views.CadPH, name="Cadastro de ph"),
    path('solo/', views.CadSolo, name="Cadastro de solo"),    
    path('sol/', views.CadSol, name="Cadastro de sol"),   
    path('espmin', views.Cadminesp, name="Cadastro de Espmin"),     
    path('irriga/', views.Cadirriga, name="Cadastro de irrigacao"),
    path('perfil_especie/<int:pk>/', views.perfil_especie, name='perfil_especie'),
    path('teste/<int:pk>/', views.perfil_planta, name='perfil planta'),
    path('Plantas', views.galeria_plantas, name='Plantas'),
    ]




