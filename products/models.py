import django.db.models
from django.db import models
from django.db.models import CharField, DecimalField


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255, blank=True)
    price = DecimalField(max_digits=10, decimal_places=2)
    on_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = CharField(max_length=64)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = CharField(max_length=64)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.CharField(max_length=9999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
