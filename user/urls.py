from django.urls import path
from . import views
urlpatterns = [
    # http://localhoust:8000/user
    path('', views.index,name="user-index"),
]
