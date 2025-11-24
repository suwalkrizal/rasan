from rest_framework import serializers
from .models import *
from apps.rasan.models import Product, FamilyPackage

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'
        extra_kwargs = {'order':{'required': True}}

    def create(self, validated_data):
        # Calculate unit_price from Product's market_price
        product = validated_data.get('product')
        if product and not validated_data.get('unit_price'):
            validated_data['unit_price'] = product.market_price
        return super().create(validated_data)

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {'total_amount': {'required':False}}

    def get_calculated_total(self, obj):
        return obj.get_total_amount()
    
        

