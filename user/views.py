from django.contrib.auth.forms import UserCreationForm
from django.db.models import F
from django.shortcuts import render, redirect
from django.views.generic import ListView

from user.forms import ProfileForm, UserRegistrationForm
from user.models import User, ProductInCart


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(
        request, 'user/register.html', {
            'form': UserCreationForm()
        }
    )


def userprofile(request):
    # TODO: use get and handle the potential exception
    profile = User.objects.filter(id=request.user.id).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(
        request, 'user/userprofile.html', {
            'form': ProfileForm(instance=profile)
        }
    )


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


class Cart(ListView):
    context_object_name = 'cart'
    template_name = 'user/cart.html'

    def get_queryset(self):
        return ProductInCart.objects.filter(user_id=self.request.user.id)
