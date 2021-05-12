from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm

from user.models import User


class ProfileForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id']
        widgets = {
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'})
        }


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'address', 'city', 'postal_code', 'email']
