from django import forms
from django.contrib.auth.forms import UserCreationForm

from user import models


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.User
        exclude = ['id', 'password', 'last_login','is_superuser','groups','user_permissions','is_staff','is_active','products_in_cart', 'date_joined']
        widgets = {
            'profile_image': forms.widgets.TextInput(attrs={'class': 'form-control'})
        }


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'address', 'city', 'postal_code', 'email']


class ContactInformationForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['address', 'city', 'postal_code', 'country']


class PaymentInformationForm(forms.ModelForm):
    class Meta:
        model = models.CreditCard
        fields = '__all__'
