from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers.order_serializer import OrderSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class OrderViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    queryset = Order.objects.all().order_by("id")
