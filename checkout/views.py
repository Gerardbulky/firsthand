from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import OrderCreateForm
from django.contrib import messages
from bag.contexts import bag_contents
from django.conf import settings
from shop.models import Product
from .models import Order, OrderItem

import stripe


def create_checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address': request.POST['street_address'],
            'postal_code': request.POST['postal_code'],
            'town': request.POST['town'],
            'city': request.POST['city'],
            'country': request.POST['country'],
        }
        order_form = OrderCreateForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            order.paid = True
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))
            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST

            """
            confirmation email for submission
            """
            messages.success(request, f'Order successfully processed! \
                Your order number is {order.id}. A confirmation \
                email will be sent to {order.email}.')

            if 'bag' in request.session:
                del request.session['bag']

            return render(request, 'checkout/order/checkout_success.html')
        else:
            messages.error(request, 'There was an error with your form. \
            Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('index'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    form = OrderCreateForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/order/checkout.html'
    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, id=id)
    messages.success(request, f'Order successfully processed! \
        Your order number is {id}. A confirmation \
        email will be sent to .')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/order/checkout_success.html'

    context = {'order': order}

    return render(request, template, context)
