from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    # http://localhoust:8000/user
    path('', lambda request: redirect('profile/', request)),
    path('add/<pk>/', views.AddToCartView.as_view()),
    path('cart/', views.Cart.as_view()),
    path('checkout/', lambda request: redirect('contact/', request)),
    path('checkout/contact/', views.ContactInformationView.as_view()),
    path('checkout/payment/', views.PaymentInformationView.as_view()),
    path('checkout/review/', views.ReviewPurchaseView.as_view()),
    path('checkout/confirmation/', views.ConfirmationView.as_view()),
    path('profile/', views.UserView.as_view(), name='profile'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout")
]
