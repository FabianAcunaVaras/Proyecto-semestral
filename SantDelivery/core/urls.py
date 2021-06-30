from django.urls import path
from .views import index, Comida , Contacto , Despacho , Sobre_nosotros


urlpatterns = [
    path('', index, name="index"),
    path('Comida', Comida, name="Comida"),
    path('Contacto', Contacto, name="Contacto"),
    path('Despacho', Despacho, name="Despacho"),
    path('Sobre_nosotros', Sobre_nosotros, name="Sobre_nosotros")

]