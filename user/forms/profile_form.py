from django.forms import ModelForm,widgets
from django.db import models
from user.models import User

class ProfileForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'name']
        widgets = {
            'profile_image': widgets.TextInput(attrs={ 'class': 'form-control'})
        }