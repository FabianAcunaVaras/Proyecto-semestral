<<<<<<< HEAD
from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'core/index.html')
=======


from django.shortcuts import render,redirect



# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def Contacto(request):
    return render(request, 'core/Contacto.html')


def Despacho(request):
    return render(request, 'core/Despacho.html')


def Sobre_Nosotros(request):
    return render(request, 'core/Sobre_Nosotros.html')

def Comida(request):
    return render(request, 'core/Comida.html')
>>>>>>> raul
