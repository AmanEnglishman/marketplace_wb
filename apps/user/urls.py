from django.urls import path

from .views import LoginAPIView, SellerRegisterView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/seller/', SellerRegisterView.as_view(), name='register-seller')
]