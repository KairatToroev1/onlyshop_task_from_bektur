from rest_framework import serializers
from cart.models import Cart, CartProduct
# from cart.serializers import CartProductSerializer

class CartSerializer(serializers.Serializer):
    class Meta:
        model = Cart
        fields = ['owner','product', ]



class CartProductSerializer(serializers.Serializer):
    class Meta:
        model = CartProduct
        fields=['person','amount', 'cart', ]

