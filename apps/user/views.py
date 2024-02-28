from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets

from apps.product.models import Cart
from apps.user.models import User
from apps.user.permissions import AnonPermission
from apps.user.serializers import MyTokenSerializer, UserSerializer


class LoginAPIView(TokenObtainPairView):
    permission_classes = (AnonPermission,)
    serializer_class = MyTokenSerializer


class SellerRegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            seller = User.objects.create(
                email=request.data['email'],
                name=request.data['name'],
                second_name=request.data['second_name'],
                phone=request.data['phone'],
                address=request.data['address'],
                is_Seller=request.data['is_Seller'],
            )
            seller.set_password(request.data['password'])
            seller.save()
            cart = Cart.objects.create(user=seller)
            cart.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellerListAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListAPIView(APIView):
    permission_classes = [permissions.AllowAny]


def get(self, request):
    is_seller = request.query_params.get('is_seller')
    if is_seller == "True":
        objects = User.objects.filter(is_Seller=True)

    elif is_seller == "False":
        objects = User.objects.filter(is_Seller=False)
    else:
        objects = User.objects.all()
    serializer = UserSerializer(objects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
