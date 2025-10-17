from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria
from django.db.models import Q

def index(request):
    categorias_todas = Categoria.objects.all()
    productos_recientes = Producto.objects.order_by('-id')[:8]
    context = {
        'categorias': categorias_todas,
        'productos': productos_recientes,
    }
    return render(request, 'catalogo/index.html', context)

def categoria_view(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    productos = categoria.productos.all()
    categorias_todas = Categoria.objects.all()
    return render(request, 'catalogo/categoria.html', {'productos': productos, 'categoria': categoria, 'categorias': categorias_todas})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    categorias_todas = Categoria.objects.all()
    return render(request, 'catalogo/detalle.html', {'producto': producto, 'categorias': categorias_todas})

def buscar(request):
    categorias_todas = Categoria.objects.all()
    query = request.GET.get('q')
    productos_resultados = Producto.objects.none()
    if query:
        productos_resultados = Producto.objects.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        ).distinct()
    context = {
        'productos': productos_resultados,
        'categorias': categorias_todas,
        'query': query
    }
    return render(request, 'catalogo/resultados_busqueda.html', context)