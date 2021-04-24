from django.shortcuts import render
from bag.contexts import bag_contents
from .models import OrderItem
from .forms import OrderCreateForm


def order_create(request):
    bag = bag_contents(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in bag:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the bag
            bag.clear()
            return render(request,
                          'checkout/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'checkout/order/create.html',
                  {'bag': bag, 'form': form})
