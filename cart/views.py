from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalogo.models import Producto, Categoria
from .cart import Cart

@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Producto, id=product_id)
    cart.add(product=product, quantity=1)
    return redirect('cart:cart_detail')

@require_POST
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Producto, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    categorias_todas = Categoria.objects.all()
    # Pasamos también el objeto 'cart' al contexto global para que el contador del menú funcione
    context = {
        'cart': cart,
        'categorias': categorias_todas,
    }
    return render(request, 'cart/cart_detail.html', context)