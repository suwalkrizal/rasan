from rest_framework import serializers
from .models import *
from apps.rasan.models import Product, FamilyPackage

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'unit_price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {'total_amount': {'required':False}}

    def get_calculated_total(self, obj):
        return obj.get_total_amount()
        

