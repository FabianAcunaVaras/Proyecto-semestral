from django.urls import path
from .views import index, Comida , Contacto , Estado_Despacho , Sobre_nosotros, Registro, Listar_Socios, Registro_Socio, Repartidor_Registro


urlpatterns = [
    path('', index, name="index"),
    path('Sobre_nosotros', Sobre_nosotros, name="Sobre_nosotros"),
    path('Comida', Comida, name="Comida"),
    path('Estado_Despacho', Estado_Despacho, name="Estado_Despacho"),
    path('Contacto', Contacto, name="Contacto"),
    path('Registro', Registro, name = "Registro"),
    path('Listar_Socios', Listar_Socios, name = "Listar_Socios"),
    path('Registro_Socio', Registro_Socio, name = "Registro_Socio"),
    path('Repartidor_Registro', Repartidor_Registro , name = "Repartidor_Registro")
    
    

]