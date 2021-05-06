from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product, Category


# Create your views here.

def overview(request):
    return render(request,
                  'products/index.html',
                  context={'categories': Category.objects.all()},
                  )


def view(request, category: str = None):
    if category.lower() in {'breakfast', 'milk', 'tableware', 'all'}:
        return render(request,
                      'products/product-list.html',
                      context={'category': category,
                               'products': Product.objects.all() if category.lower() == 'all' else Product.objects.filter(
                                   category__name__contains=category)}
                      )
    else:
        return HttpResponse(f'404: There is no category {category}', status=404)
