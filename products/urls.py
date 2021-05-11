from django.urls import include, path

from . import views

urlpatterns = [
    # https://localhoust:8000/prooducts
    path('', views.CategoryList.as_view()),
    path('<str:category>/', views.ProductList.as_view()),
    path('product/<pk>/', views.ProductDetailView.as_view()),
    path('<str:category>/search/', views.SearchResult.as_view(), name='product-search-results'),
    path('aboutus', views.about, name="aboutus"),
    path('contact', views.contact, name="contact")
]
