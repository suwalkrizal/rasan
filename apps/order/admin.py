from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'package', 'status', 'payment_method', 'order_date', 'total_amount',)
    search_fields = ('status', 'payment_method', 'order_date')
    list_filter = ('user__username', 'package__package_name')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'unit_price')
    search_fields = ('order__status',)
    list_filter = ('product__product_name',)