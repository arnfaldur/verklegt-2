from django.urls import path
from . import views
urlpatterns = [
    # http://localhoust:8000/cart
    path('', views.index,name="index"),
]
