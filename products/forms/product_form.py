from django.forms import ModelForm, widgets
from django import forms
from products.models import Product, Image


class ProductCreateForm(ModelForm):
    imgage = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Product
        exclude = [ 'id' ]
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
        }

# class ImageForm(ModelForm):
#     class Meta:
#         model = Image
#         exclude = ['id']
#         widgets ={
#             'image': widgets.TextInput
#         }
