from django.shortcuts import render
from cart.cart import Cart
from .models import OrderItem
from .forms import OrderCreateForm

from django.conf import settings

import stripe


def order_create(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():

            total = cart.get_total_price
            stripe_total = round(total * 100)
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )

            print(intent)
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
