# fabrica/views.py
from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from .models import Producto
from .forms import ProductoForm
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'fabrica/listar_productos.html', {'productos': productos})

def fabrica_view(request):
    productos = Producto.objects.all()
    return render(request, 'fabrica/fabrica.html', {'productos': productos})


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/fabrica/')
    else:
        form = ProductoForm()
    return render(request, 'fabrica/agregar_producto.html', {'form': form})


def mostrar_cadena(request, cadena):
    if cadena:
        return HttpResponse(f"El username es: {cadena}")
    else:
        return HttpResponse("La cadena está vacía")
    

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'fabrica/detalle_producto.html', {'producto': producto})