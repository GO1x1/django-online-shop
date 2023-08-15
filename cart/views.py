
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from OnlineShop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.conf import settings


from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from OnlineShop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                                  update_quantity=cd['update'])
    return redirect('shop_single', product.slug)

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_quantity_plus(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.quantity_plus(product)
    return redirect('cart_detail')
def clear_all(request):
    cart = Cart(request)
    cart.clear_all()
    return redirect('cart_detail')

def cart_quantity_min(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.quantity_min(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    print(cart.session)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                                        initial={
                                            'quantity': item['quantity'],
                                            'update': True
                                        })
    return render(request, 'cart/cartdetail.html', {'cart': cart})