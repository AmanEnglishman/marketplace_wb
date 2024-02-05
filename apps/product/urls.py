from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    ProductListAPIView,
    ProductCreateAPIView,
    CategoryCreateAPIView,
    CategoryListAPIView,
    ProductDetailAPIView,
    ProductDeleteAPIView,
    ProductUpdateAPIView,
    ProductViewSet,
    ProductFilterListAPI,
    CartAPIView,

)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('', ProductListAPIView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='delete-product'),
    path('products/<int:pk>/update/', ProductUpdateAPIView.as_view(), name='update-product'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('filter/', ProductFilterListAPI.as_view(), name='product-filter'),
    path('cart/<int:id>/', CartAPIView.as_view(), name='cart'),
]
