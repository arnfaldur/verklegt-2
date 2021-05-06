import django.db.models
from django.db import models
from django.db.models import CharField, DecimalField


class ProductCategory(models.Model):
    name = CharField(max_length=64)

def __str__(self):
    return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = DecimalField(max_digits=10, decimal_places=2)
    on_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.CharField(max_length=9999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
