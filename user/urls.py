from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    # http://localhoust:8000/user
    path('', views.userprofile, name="user"),
    path('add/<pk>', views.add_to_cart),
    path('cart', views.Cart.as_view()),
    path('profile', views.userprofile, name="profile"),
    path('register', views.register, name="register"),
    path('login', LoginView.as_view(template_name='user/login.html'), name="login"),
    path('logout', LogoutView.as_view(next_page='login'), name="logout")
]
