from django.urls import path
from .views import LoginAPIView, SellerRegisterView, SellerListAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('sellers/', SellerListAPIView.as_view(), name='seller-list'),
    path('register/', SellerRegisterView.as_view(), name='register'),
]
