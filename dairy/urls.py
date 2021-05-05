from django.urls import path
from . import views
urlpatterns = [
    # http://localhoust:8000/dairy
    path('', views.index,name="dairy-index"),
]
