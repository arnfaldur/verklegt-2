from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="products-index"),
    path("breakfast", views.breakfast, name="products-breakfast"),
]
