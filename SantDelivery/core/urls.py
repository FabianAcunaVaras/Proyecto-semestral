from django.urls import path
<<<<<<< HEAD
from .views import index


urlpatterns = [
    path('', index, name="index"),    
=======
from .views import index, Comida , Contacto , Despacho , Sobre_Nosotros

urlpatterns = [
    path('', index, name="index"),
    path('Comida', Comida, name="Comida"),
    path('Contacto', Contacto, name="Contacto"),
    path('Despacho', Despacho, name="Despacho"),
    path('Sobre_Nosotros', Sobre_Nosotros, name="Sobre_Nosotros")
>>>>>>> raul
]