from django.shortcuts import render,redirect
from core.forms import ClientesForm, SociosForm, RepartidorForm
from .models import Socios, Repartidor


# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def Contacto(request):
    return render(request, 'core/Contacto.html')


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


def Registro_Socio(request):
    datos = {
        'form' : SociosForm()
    }

    if request.method == 'POST':
        formulario = SociosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Usuario Ingresado Correctamente"
    return render(request, 'core/Registro_Socio.html',datos)


def Repartidor_Registro(request):
    datos = {
        'form' : RepartidorForm()
    }

    if request.method == 'POST':
        formulario = RepartidorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Usuario Ingresado Correctamente"
    return render(request, 'core/Repartidor_Registro.html',datos)


def Estado_Despacho(request):
    Rp = Repartidor.objects.all()
    datos = {
        "Repartidor" : Rp
    }
    return render(request, 'core/Estado_Despacho.html',datos)