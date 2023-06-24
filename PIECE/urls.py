
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage" ),
    path('cadastrarespecie/', views.Cad, name="Cadastro de Espécie" ),
    path('minerios/', views.Cadmin, name="Cadastro de minerio"),
    path('estacao/', views.Cadest, name="Cadastro de estacao"),
    path('ph/', views.CadPH, name="Cadastro de ph"),
    path('solo/', views.CadSolo, name="Cadastro de solo"),    
    path('sol/', views.CadSol, name="Cadastro de sol"),   
    path('irriga/', views.Cadirriga, name="Cadastro de irrigacao"),
    path('buscar_especie/', views.buscar_especie, name='buscar_especie'),
    path('perfil_especie/<int:pk>/', views.perfil_especie, name='perfil_especie'),
]




