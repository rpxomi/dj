from django.shortcuts import render
from .models import Producto

# CREATE YOUR VIEWS HERE
# 'productos': es la plantilla de html
# productos: es la variable que contiene los datos, para la plantilla
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})
