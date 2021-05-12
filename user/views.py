from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F, Sum
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView

from user.forms import ProfileForm, UserRegistrationForm
from user.models import User, ProductInCart


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'user/register.html'
    success_url = '/'


class UserView(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    template_name = 'user/user_profile.html'

    def get_object(self, queryset=None):
        return self.request.user


def add_to_cart(request, pk):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        # Create product in cart if none exists
        obj, created = user.productincart_set.get_or_create(
            product_id=pk,
            defaults={'user_id': user.id, 'quantity': 1}
        )
        # if one exists: increment it's quantity
        if not created:
            obj.quantity = F('quantity') + 1
            obj.save()
    # TODO: else: send user to login page
    else:
        redirect('/user/login')
    return redirect('/user/cart')


class Cart(LoginRequiredMixin, ListView):
    context_object_name = 'cart'
    template_name = 'user/cart.html'

    def get_queryset(self):
        return ProductInCart.objects \
            .filter(user_id=self.request.user.id) \
            .annotate(total=F('product__price') * F('quantity'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            self.get_queryset().aggregate(total_price=Sum('total'))
        )
        return context
