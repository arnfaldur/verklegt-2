from django.shortcuts import render
from products.models import Product


# Create your views here.

def view(request, category=None):
    if category in {'breakfast', 'milk', 'tableware'}:
        return render(request,
                      'products/product-list.html',
                      context={'category': category,
                               'products': Product.objects.filter(category__name__contains=category)}
                      )
    else:
        return render(request,
                      'products/index.html',
                      context={'category': None},
                      )
