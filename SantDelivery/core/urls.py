from django.urls import path
from .views import index, Comida , Contacto , Despacho , Sobre_nosotros, Registro, Listar_Socios


urlpatterns = [
    path('', index, name="index"),
    path('Sobre_nosotros', Sobre_nosotros, name="Sobre_nosotros"),
    path('Comida', Comida, name="Comida"),
    path('Despacho', Despacho, name="Despacho"),
    path('Contacto', Contacto, name="Contacto"),
    path('Registro', Registro, name = "Registro"),
    path('Listar_Socios', Listar_Socios, name = "Listar_Socios")
    
    

]