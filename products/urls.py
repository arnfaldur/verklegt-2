from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.view, name="products-index"),
    path("<str:category>", views.view, name="products-list"),
]
