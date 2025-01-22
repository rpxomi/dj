from django.urls import path
from . import views

# views.lista_productos, es la función que se encargará de manejar la petición
# name="lista_productos", es una variable que se usará para referenciar esta URL dentro del mismo código de Django
urlpatterns = [
    path("", views.lista_productos, name="lista_productos"),
]
