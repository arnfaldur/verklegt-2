import django.db.models
from django.db import models
from django.db.models import CharField, DecimalField

# Create your models here.

# TODO: make this into an actual database

database = [
    {'category': 'breakfast', 'name': 'Cheerios', 'price': '200'},
    {'category': 'breakfast', 'name': 'CocoPuffs', 'price': '250'},
    {'category': 'breakfast', 'name': 'Corn Flakes', 'price': '200'},
    {'category': 'breakfast', 'name': 'Lucky Charms', 'price': '300'},
]


class Product(models.Model):
    name = CharField(max_length=128, primary_key=True)
    price = DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = CharField(max_length=64, primary_key=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


def populate_database():
    cheerios = Product(name='Cheerios', price=200)
    cheerios.save()
    cocoa_puffs = Product(name='Cocoa Puffs', price=250)
    cocoa_puffs.save()
    corn_flakes = Product(name='Corn Flakes', price=200)
    corn_flakes.save()
    lucky_charms = Product(name='Lucky Charms', price=300)
    lucky_charms.save()
    category = Category(name='Breakfast')
    category.products.add(cheerios, cocoa_puffs, corn_flakes, lucky_charms)


def get_breakfasts():
    return database
