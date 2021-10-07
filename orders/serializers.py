from rest_framework import serializers
from orders.models import Order

class OrderSerializer(serializers.Serializer):
    class Meta:
        model = Order
        fields = [' created_at','products_list','total_amount','estimated_delivery_date ',]