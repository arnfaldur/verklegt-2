from django.views.generic import ListView, DetailView
from products.models import Product, Category
from django.shortcuts import render


class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'products/index.html'


class ProductList(ListView):
    model = Product

    def get_queryset(self):
        # if the url is /all, return all products from the products model
        # otherwise only return the products from the category /<category>
        return Product.objects.all() if self.kwargs['category'] == 'all' \
            else Product.objects.filter(category__name__contains=self.kwargs['category'])

    def get_context_data(self, **kwargs):
        # Get the default context made by ListView
        context = super().get_context_data(**kwargs)

        # add the name of the category to the context
        context['category'] = self.kwargs['category']

        return context


class SearchResult(ProductList):
    template_name = 'products/product_list.html'

    def get_queryset(self):
        search = self.request.GET.get('s')
        sort = self.request.GET.get('sort')
        filter = self.request.GET.get('filter')

        # Replace the product list with a reduced set of products
        if search:
            return super().get_queryset().filter(name__contains=search)

        if sort:
            return super().get_queryset().order_by(sort)

        if filter:
            return super().get_queryset()


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'


def about(request):
    return render(request, 'products/about.html')


def contact(request):
    return render(request, 'products/contact.html')


#@login_required
def create_product(request):
    if request.method == 'POST':
        print(1)
    else:
        print(2)
        # TODO: Instance new productCreateForm()
    return render(
        request, 'products/create_product.html', {
            'form': form
        }
    )
