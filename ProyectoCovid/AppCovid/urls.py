"""ProyectoCovid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from AppCovid import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path("guantes", views.guantes, name= "Guantes"),
    path("barbijos", views.barbijos, name= "Barbijos"),
    path("oximetros", views.oximetros, name= "Oximetros"),
    path("barbijosFormulario/", views.barbijosFormulario, name= "Formulario de Barbijos"),
    path("busquedaDeBarbijos", views.busquedaDeBarbijos, name=  "Busqueda de Barbijos"),
    path("buscar/", views.buscar),
    path("guantesFormulario/", views.guantesFormulario, name= "Formulario de Guantes"),
    path("eliminarGuante/<marca_para_borrar>", views.eliminarGuante, name= "EliminarGuante"),
    path("editarBarbijo/<marca_para_editar>", views.editarBarbijo, name= "EditarBarbijo"),
    path("eliminarBarbijo/<marca_para_borrar>", views.eliminarBarbijo, name= "EliminarBarbijo"),
    path("leerBarbijos",views.leerBarbijos, name= "LeerBarbijos"),


    path("leerGuantes",views.leerGuantes, name= "LeerGuantes"),
]
