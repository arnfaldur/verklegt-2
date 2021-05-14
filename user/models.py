from django.db import models
from django.db.models import CharField, DateField, ImageField, ManyToManyField, \
    PositiveSmallIntegerField
from django.contrib.auth.models import AbstractUser

from django_countries.fields import CountryField

from products.models import Product


class User(AbstractUser):
    username = None
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'This email address is already in use.'
        }
    )
    address = CharField(max_length=256, blank=True)
    city = CharField(max_length=256, blank=True)
    postal_code = CharField(max_length=16, blank=True)
    country = CountryField(blank_label='select country', blank=True)
    picture = CharField(max_length=9999)
    products_in_cart = ManyToManyField(Product, through='ProductInCart')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'auth_user'


class ProductInCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class CreditCard(models.Model):
    credit_card = CharField(max_length=19)
    cvc = PositiveSmallIntegerField()
    expiry = DateField()
