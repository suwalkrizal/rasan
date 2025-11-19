from django.urls import path
from .views import *

urlpatterns = [
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail'),

    path('order_items/', OrderItemListCreateAPIView.as_view(), name='orderitem-list-create'),
    path('order_items/<int:pk>/', OrderItemDetailAPIView.as_view(), name='orderitem-detail'),
]