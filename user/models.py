from django.db import models
from django.db.models import CharField, ImageField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = CharField(max_length=256, blank=True)
    city = CharField(max_length=256, blank=True)
    postal_code = CharField(max_length=16, blank=True)
    picture = ImageField(blank=True)

    class Meta:
        db_table = 'auth_user'

