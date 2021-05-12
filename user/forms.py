from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm

from user.models import User


class ProfileForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'password', 'last_login','is_superuser','groups','user_permissions','is_staff','is_active','products_in_cart']
        widgets = {
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'})
        }


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'address', 'city', 'postal_code', 'email']
