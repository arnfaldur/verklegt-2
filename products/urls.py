from django.urls import include, path

from . import views

urlpatterns = [
    # https://localhoust:8000/prooducts
    path('', views.CategoryList.as_view()),
    path('category/<str:category>/', views.ProductList.as_view()),
    path('category/<str:category>/search/', views.SearchResult.as_view(),
        name='product-search-results'),
    path('product/<pk>/', views.ProductDetailView.as_view()),
    path('create_product/', views.CreateProductView.as_view(), name="create_product"),
    path('delete_product/<pk>/', views.DeleteProductView.as_view(), name="delete_product"),
    path('update_product/<pk>/', views.UpdateProductView.as_view(), name="update_product"),
]
