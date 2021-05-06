from django.shortcuts import render
from products.models import Product


# Create your views here.

def index(request):
    return render(request, 'products/index.html')


def breakfast(request):
    return render(request, 'products/breakfast/index.html',
                  context={'breakfasts': Product.objects.all()})
