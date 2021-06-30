from django.core.exceptions import ValidationError
from core.forms import ProveedoresForm, PaisForm
from django.shortcuts import render,redirect
from .models import Proveedores

# Create your views here.
def index(request):
    return render(request, 'core/index.html')


