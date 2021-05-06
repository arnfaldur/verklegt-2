from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.overview),
    path("<str:category>", views.view),
]
