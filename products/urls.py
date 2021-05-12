from django.urls import include, path

from . import views

urlpatterns = [
    # https://localhoust:8000/prooducts
    path('', views.CategoryList.as_view()),
    path('<str:category>/', views.ProductList.as_view()),
    path('product/<pk>/', views.ProductDetailView.as_view()),
    path('<str:category>/search/', views.SearchResult.as_view(), name='product-search-results'),
    path('create_product/', views.create_product, name="create_product"),
    path('delete_product/<pk>/', views.delete_product, name="delete_product"),
    path('update_product/<pk>/', views.update_product, name="update_product"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact")
]
