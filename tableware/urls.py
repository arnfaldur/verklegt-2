from django.urls import path
from . import views
urlpatterns = [
    # http://localhoust:8000/tableware
    path('', views.index,name="tableware-index"),
]
