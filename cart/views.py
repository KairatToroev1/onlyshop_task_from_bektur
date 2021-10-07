from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from cart.models import Cart, CartProduct
from cart.serializers import CartSerializer, CartProductSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, ]

class CartProductViewSet(ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer
    permission_classes = [IsAuthenticated, ]
