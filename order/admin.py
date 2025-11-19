from django.contrib import admin
from .models import *

# Register your models here.

# @admin.register(MonthlyRasanTemplate)
# class MonthlyRasanTemplateAdmin(admin.ModelAdmin):
#     list_display = ('template_name', 'user')
#     search_fields = ('template_name', 'user__username')
#     list_filter = ('user',)

# @admin.register(MonthlyRasanItem)
# class MonthlyRasanItemAdmin(admin.ModelAdmin):
#     list_display = ('template', 'product', 'quantity')
#     search_fields = ('template__template_name', 'product__product_name')
#     list_filter = ('template',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'package', 'delivery_address', 'status', 'payment_method', 'order_date', 'total_amount')
    search_fields = ('user__username',)
    list_filter = ('user',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'unit_price', 'total_price')
    search_fields = ('order__id', 'product__product_name')
    list_filter = ('order',)