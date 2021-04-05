from django.shortcuts import render
from cart.cart import Cart
from .models import OrderItem
from .forms import OrderCreateForm


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            return render(request,
                          'checkout/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'checkout/order/create.html',
                  {'cart': cart, 'form': form,
                   'stripe_public_key': 'pk_test_51IRDEYI93ifnqnA18YPxFgcgWkIPir6YSxh1038ymbn48JgXIhOx7UTCdp8F9M4N602Bs1E97zupGE9FZQNkb95G00DAvzFxPi',
                   'client_secret': 'test client secret'})
