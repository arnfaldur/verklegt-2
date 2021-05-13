from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F, Sum
from django.views.generic import CreateView, ListView, RedirectView, UpdateView

from user.forms import ContactInformationForm, PaymentInformationForm, ProfileForm, \
    UserRegistrationForm
from user.models import ProductInCart


class AuthenticatedUserMixin(LoginRequiredMixin):
    def get_object(self, queryset=None):
        return self.request.user


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'user/register.html'
    success_url = '/'


class UserView(AuthenticatedUserMixin, UpdateView):
    form_class = ProfileForm
    template_name = 'user/user_profile.html'
    success_url = '/user/profile/'

    def profile(self, request):
        profile = User.objects.filter(email=request.email).first()
        if request.method == 'POST':
            form = ProfileForm(instance=profile, data=request.POST)
            if form.is_valid():
                profile = form.save(comit=False)
                profile.email = request.email
                profile.save()
                return redirevt('profile')
            return render(
                request, 'user/user_profile.html', {
                    'form': ProfileForm(instance=profile)
                }
            )


class AddToCartView(LoginRequiredMixin, RedirectView):
    url = '/user/cart'

    def get(self, request, *args, **kwargs):
        # get_or_create the item in the user's cart
        obj, created = request.user.productincart_set.get_or_create(
            product_id=kwargs['pk'],
            defaults={'user_id': request.user.id, 'quantity': 1}
        )
        # if one exists: increment it's quantity
        if not created:
            obj.quantity = F('quantity') + 1
            obj.save()

        return super().get(request, *args, **kwargs)


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


class ContactInformationView(AuthenticatedUserMixin, UpdateView):
    form_class = ContactInformationForm
    template_name = 'user/checkout/contact_information.html'
    success_url = '/user/checkout/payment/'


class PaymentInformationView(AuthenticatedUserMixin, UpdateView):
    form_class = PaymentInformationForm
    template_name = 'user/checkout/payment_information.html'
    success_url = '/user/checkout/review/'


class ReviewPurchaseView(Cart):
    template_name = 'user/checkout/review.html'
    success_url = '/user/checkout/confirmation/'


class ConfirmationView(Cart):
    template_name = 'user/checkout/confirmation.html'


class Checkout(Cart, UpdateView):
    form_class = ProfileForm
    # TODO: add overview of shipping address etc.

    def get_context_data(self, **kwargs):
        context = Cart.get_context_data(self, **kwargs)
        return context
