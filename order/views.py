from django.shortcuts import render
from rest_framework import status
from.models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class OrderListCreateAPIView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class OrderDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return None

    def get(self, request, pk):
        order = self.get_object(pk)
        if order is None:
            return Response({'error': 'Order not found'}, status=404)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    def put(self, request, pk):
        order = self.get_object(pk)
        if not order:
            return Response({'error': 'Order not found'}, status=404)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        order = self.get_object(pk)
        if not order:
            return Response({'error': 'Order not found'}, status=404)
        order.delete()
        return Response({'detail': 'order deletes successfully'}, status=204)
    

class OrderItemListCreateAPIView(APIView):
    def get(self, request):
        items = OrderItem.objects.all()
        serializer = OrderItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            # Calculate total_price if not provided
            quantity = serializer.validated_data['quantity']
            unit_price = serializer.validated_data['unit_price']
            serializer.validated_data['total_price'] = quantity * unit_price
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return OrderItem.objects.get(pk=pk)
        except OrderItem.DoesNotExist:
            return None

    def get(self, request, pk):
        item = self.get_object(pk)
        if not item:
            return Response({'error': 'OrderItem not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrderItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk)
        if not item:
            return Response({'error': 'OrderItem not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrderItemSerializer(item, data=request.data)
        if serializer.is_valid():
            # Recalculate total_price
            quantity = serializer.validated_data.get('quantity', item.quantity)
            unit_price = serializer.validated_data.get('unit_price', item.unit_price)
            serializer.validated_data['total_price'] = quantity * unit_price
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk)
        if not item:
            return Response({'error': 'OrderItem not found'}, status=status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response({'detail': 'OrderItem deleted successfully'}, status=status.HTTP_204_NO_CONTENT)   
