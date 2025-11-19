from django.db import models
from django.conf import settings
from rasan.models import Product, FamilyPackage

# Create your models here.
# class MonthlyRasanTemplate(models.Model):
#     template_name = models.CharField(max_length=100)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='templates')

#     class Meta:
#         db_table = '"order"."monthly_rasan_template"'

# class MonthlyRasanItem(models.Model):
#     template = models.ForeignKey(MonthlyRasanTemplate, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()

#     class Meta:
#         db_table = '"order"."monthly_rasan_item"'

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    PAYMENT_METHOD_CHOICES = (
        ('cash_on_delivery', 'Cash_on_Delivery'),
        ('esewa', 'Esewa'),
        ('khalti', 'Khalti'),
        ('bank_transfer', 'Bank_Transfer'),
        ('card_payment', 'Card_Payment'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    package = models.ForeignKey(FamilyPackage, on_delete=models.CASCADE, null=True, blank=True)
    delivery_address = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES, default='cash_on_delivery')
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField()

    class Meta:
        db_table = '"order"."order"'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.FloatField(null=True, blank=True)
    total_price = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = '"order"."order_item"'