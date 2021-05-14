from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from products.models import Product, Category, Attribute
from products.forms import ProductForm


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
            else Product.objects.filter(category__name__iexact=self.kwargs['category'])

    def get_context_data(self, **kwargs):
        # Get the default context made by ListView
        context = super().get_context_data(**kwargs)

        # add the name of the category to the context
        context['category'] = self.kwargs['category']

        context['attributes'] = Attribute.objects.all()

        return context


class SearchResult(ProductList):
    template_name = 'products/product_list.html'

    def get_queryset(self):
        search = self.request.GET.get('s')
        sort = self.request.GET.get('sort')
        filtered = self.request.GET.getlist('filter')
        sale = self.request.GET.get('sale')

        results = Product.objects.all()
        # Replace the product list with a reduced set of products
        if search and len(search) > 0:
            results = results.filter(name__icontains=search)

        if sort:
            results = results.order_by(sort)

        if filtered:
            if filtered == 'All':
                return Product.objects.all()
            results = results.filter(attribute__name__in=filtered)

        if sale:
            results = results.filter(on_sale=True)
        return results.distinct()


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'


class CreateProductView(PermissionRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = 'standard_form.html'
    permission_denied_message = 'You do not have sufficient privileges to create products'
    permission_required = 'products.add_product'


class UpdateProductView(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'standard_form.html'
    permission_denied_message = 'You do not have sufficient privileges to update products'
    permission_required = 'products.change_product'


class DeleteProductView(PermissionRequiredMixin, DeleteView):
    model = Product
    form_class = ProductForm
    template_name = 'standard_form.html'
    permission_denied_message = 'You do not have sufficient privileges to delete products'
    permission_required = 'products.delete_product'
