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
        products = Product.objects.all()
        return products if self.kwargs['category'] == 'all' else Product.objects.filter(
            category__name__contains=self.kwargs['category'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['category'] = self.kwargs['category']
        context['products'] = self.get_queryset()

        return context


class ProductDetailView(DetailView):
    model = Product

    context_object_name = 'product'

def create_product():
    if request.method == 'POST':
        print(1)
    else:
        print(2)
        # TODO: Instance new productCreateForm()
    return render(request,'products/create_product.html',{
        'form': form
    })