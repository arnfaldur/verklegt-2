from django.views.generic import ListView, DetailView
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
        # if the url is /all, return all products from the products model
        # otherwise only return the products from the category /<category>
        return Product.objects.all() if self.kwargs['category'] == 'all' else Product.objects.filter(
            category__name__contains=self.kwargs['category'])

    def get_context_data(self, **kwargs):
        # Get the default context made by ListView
        context = super().get_context_data(**kwargs)

        # add the name of the category to the context
        context['category'] = self.kwargs['category']
        # add the queried products to the context for display
        context['products'] = self.get_queryset()

        return context


class ProductDetailView(DetailView):
    model = Product

    context_object_name = 'product'


class SearchResult(ProductList):
    template_name = 'products/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['products'] = self.get_queryset().filter(name__contains=self.request.GET.get('s'))

        return context

#@login_required
def create_product(request):
    if request.method == 'POST':
        print(1)
    else:
        print(2)
        # TODO: Instance new productCreateForm()
    return render(request, 'products/create_product.html', {
        'form': form
    })
