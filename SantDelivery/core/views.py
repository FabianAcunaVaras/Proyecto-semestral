from django.shortcuts import render,redirect
from core.forms import ClientesForm
from .models import Socios


# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def Contacto(request):
    return render(request, 'core/Contacto.html')


def Despacho(request):
    return render(request, 'core/Despacho.html')


def Sobre_nosotros(request):
    return render(request, 'core/Sobre_nosotros.html')

def Comida(request):
    return render(request, 'core/Comida.html')

def Registro(request):
    datos = {
        'form' : ClientesForm()
    }

    if request.method == 'POST':
        formulario = ClientesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Usuario Ingresado Correctamente"
    return render(request, 'core/Registro.html',datos)

def Listar_Socios(request):
    Ls = Socios.objects.all()
    datos = {
        "Socios" : Ls
    }
    return render(request, 'core/Listar_Socios.html',datos)