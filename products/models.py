import django.db.models
from django.db import models
from django.db.models import CharField, DecimalField


# Create your models here.

class Product(models.Model):
    name = CharField(max_length=128, primary_key=True)
    price = DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.BigAutoField
    name = CharField(max_length=64, primary_key=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
