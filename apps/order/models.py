from django.db import models
from django.conf import settings
from apps.rasan.models import Product, FamilyPackage
# from django.db.models.signals import post_save
# from django.dispatch import receiver



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
    total_amount = models.FloatField(null=True, blank=True)

    def get_total_amount(self):
        return sum(item.quantity * item.unit_price for item in self.items.all())
    
# @receiver(post_save, sender='order')

    def save(self, *args, **kwargs):
        if self.total_amount is None:
            self.total_amount = self.get_total_amount()
        super().save(*args, **kwargs)

    class Meta:
        db_table = '"order"."order"'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.FloatField(null=True, blank=True)
    

    class Meta:
        db_table = '"order"."order_item"'