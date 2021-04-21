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
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart = Cart(request)
            current_bag = {{cart.get_total_price}}
            total = current_bag
            stripe_total = total
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )
            print(intent)

            context = {'order': order,
                       'stripe_public_key': stripe_public_key,
                       'client_secret': intent.client_secret,
                       }
            template = 'checkout/order/create.html'

            return render(request, template, context)

    else:
        form = OrderCreateForm()

        template = 'checkout/order/create.html'
        context = {
            'cart': cart, 'form': form,
            'stripe_public_key': stripe_public_key,
            'stripe_secret_key': stripe_secret_key,
        }
    return render(request, template, context)

