from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from products.models import Product, Category


class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'

    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.all()
        return context


class ProductList(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.all() if self.kwargs['category'] == 'all' else Product.objects.filter(
            category__name__contains=self.kwargs['category'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['category'] = self.kwargs['category']
        context['products'] = self.get_queryset()

        return context
