from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.CategoryList.as_view()),
    path('<str:category>/', views.ProductList.as_view()),
]
