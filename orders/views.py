from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from orders.models import Order
from orders.serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, ]
