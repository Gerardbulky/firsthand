from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Category, Product

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'shop/index.html')


def product_list(request, category_slug=None):
    query = None
    category = None
    categories = None

    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(Category__slug__in=categories)
            categories = Category.objects.filter(slug__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('index'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'search_term': query,
                   'current_categories': categories})




def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    return render(request,
                  'shop/product/detail.html',
                  {'product': product})

