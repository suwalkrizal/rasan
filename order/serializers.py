from rest_framework import serializers
from .models import *
from rasan.models import Product, FamilyPackage

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.product_name')

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'unit_price', 'total_price']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    package_name = serializers.ReadOnlyField(source='package.package_name')

    class Meta:
        model = Order
        fields = ['id', 'user', 'package', 'package_name', 'delivery_address', 'status', 'payment_method', 'order_date', 'total_amount', 'order_items']
        

