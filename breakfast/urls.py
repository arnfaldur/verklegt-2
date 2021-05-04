from django.urls import path
from . import views
urlpatterns = [
    # http://localhoust:8000/brekfast
    path('', views.index,name="index"),
]
