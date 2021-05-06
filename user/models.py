from django.db import models
from django.db.models import CharField, ImageField


# Create your models here.


class User(models.Model):
    name = CharField(max_length=128)
    address = CharField(max_length=256)
    city = CharField(max_length=256)
    postal_code = CharField(max_length=16)
    email = models.EmailField()
    username = CharField(max_length=256)
    password = CharField(max_length=256)
    picture = ImageField()

