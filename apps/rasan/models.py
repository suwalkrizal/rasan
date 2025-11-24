from django.db import models

# Create your models here.
class Category(models.Model):

    category_name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = '"inventory"."category"'


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=100)
    unit = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = '"inventory"."sub_category"'

    
class Brand(models.Model):
    brand_name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        db_table = '"inventory"."brand"'

    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    market_price = models.FloatField()
    net_quantity = models.IntegerField()

    class Meta:
        db_table = '"inventory"."product"'

    
class FamilyPackage(models.Model):
    package_name = models.CharField(max_length=100)
    family_size_min= models.IntegerField()
    family_size_max = models.IntegerField()
    base_price = models.FloatField()

    class Meta:
        db_table = '"inventory"."family_package"'

    
class PackageItem(models.Model):
    package = models.ForeignKey(FamilyPackage, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = '"inventory"."package_item"'

class Supplier(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length= 10, choices= GENDER_CHOICES, blank=True, null=True)
    image = models.ImageField(upload_to='supplier_images/', blank=True, null=True)
    pan_no = models.CharField(max_length=20, null= True, blank=True)
    pan_image = models.ImageField(upload_to='supplier_pan_images/', null= True, blank=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    contact_no = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = '"inventory"."supplier"'

class SupplierProduct(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supply_price = models.FloatField()

    class Meta:
        db_table = '"inventory"."supplier_product"'