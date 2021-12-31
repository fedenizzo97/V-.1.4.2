from django.shortcuts import render
from django.http import HttpResponse

from AppCovid.models import Guantes, Oximetros, Barbijos
from AppCovid.forms import BarbijosFormulario, GuantesFormulario
# Create your views here.

def inicio(request):

    return render(request, "AppCovid/inicio.html")

def guantes(request):

    return render(request, "AppCovid/guantes.html")

def barbijos(request):
    
    return render(request, "AppCovid/barbijos.html")

def oximetros(request):
    
    return render(request, "AppCovid/oximetros.html")

def barbijosFormulario(request):
    if request.method == "POST":

        miFormulario = BarbijosFormulario(request.POST)
        
        if miFormulario.is_valid():

            informacion= miFormulario.cleaned_data

            barbijoInst= Barbijos(marca= informacion["marca"], tamanio= informacion["tamanio"], precio= request.POST ["precio"])

            barbijoInst.save()  

            return render(request,"AppCovid/inicio.html")

    else:

        miFormulario = BarbijosFormulario()

    return render(request, "AppCovid/barbijosFormulario.html", {"miFormulario": miFormulario})

def busquedaDeBarbijos(request):

    return render(request, "AppCovid/busquedaDeBarbijos.html")


def buscar(request):

    if request.GET["marca"]:
        
        marca= request.GET["marca"]

        barbijo= Barbijos.objects.filter(marca__icontains= marca)

    #respuesta= f"Estoy buscando a: {request.GET['marca']}"
        return render(request, "AppCovid/resultadoBusqueda.html", {"barbijo": barbijo, "marca":marca})
    else: 
        respuesta= "Por favor mandame mas informacion, sino no puedo ayudarte"
    return HttpResponse(respuesta)

def leerGuantes(request):

    guante= Guantes.objects.all()

    diccionario1= {"guante": guante}
    
    return render(request, "AppCovid/leerGuantes.html",diccionario1)

def leerBarbijos(request):

    barbijo= Barbijos.objects.all()

    diccionario1= {"barbijo": barbijo}
    
    return render(request, "AppCovid/leerBarbijos.html",diccionario1)


def guantesFormulario(request):
    if request.method == "POST":

        miFormulario = GuantesFormulario(request.POST)
        
        if miFormulario.is_valid():

            informacion1= miFormulario.cleaned_data

            guanteInst= Guantes(marca= informacion1["marca"], tamanio= informacion1["tamanio"], precio= request.POST ["precio"], esPremium= informacion1.POST["esPremium"])

            guanteInst.save()  

            return render(request,"AppCovid/inicio.html")

    else:

        miFormulario = GuantesFormulario()

    return render(request, "AppCovid/guantesFormulario.html", {"miFormulario": miFormulario})



def eliminarGuante(request, marca_para_borrar ):

    guanteQueQuieroBorrar= Guantes.objects.get(marca= marca_para_borrar)

    guanteQueQuieroBorrar.delete()

    guante =Guantes.objects.all()

    return render(request, "AppCovid/leerGuantes.html", {"guante": guante})

def eliminarBarbijo(request, marca_para_borrar ):

    barbijoQueQuieroBorrar= Barbijos.objects.get(marca= marca_para_borrar)

    barbijoQueQuieroBorrar.delete()

    barbijo =Barbijos.objects.all()

    return render(request, "AppCovid/leerBarbijos.html", {"barbijo": barbijo})


def editarBarbijo(request, marca_para_editar):

    barbijo= Barbijos.objects.get(marca_para_editar)

    if request.method == "POST":

            miFormulario = BarbijosFormulario(request.post)
            
            if miFormulario.is_valid():

                informacion1= miFormulario.cleaned_data

            
                barbijo.marca= informacion1["marca"], 
                barbijo.tamanio= informacion1["tamanio"], 
                barbijo.precio= informacion1["precio"], 
                

                barbijo.save()

                return render(request,"AppCovid/inicio.html")

    else:

        miFormulario = BarbijosFormulario(initial={"marca": barbijo.marca, "tamanio": barbijo.tamanio, "precio": barbijo.precio})

    return render(request, "AppCovid/editarBarbijo.html", {"miFormulario": miFormulario, "marca_para_editar": marca_para_editar})

