from django.db import models
from django.db.models import CharField, ImageField, ManyToManyField
from django.contrib.auth.models import AbstractUser

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
    picture = ImageField(blank=True)
    products_in_cart = ManyToManyField(Product, through='ProductInCart')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'auth_user'


class ProductInCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
