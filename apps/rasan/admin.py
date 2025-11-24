from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory_name', 'category', 'unit')
    search_fields = ('subcategory_name',)
    list_filter = ('category',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)
    search_fields = ('brand_name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'subcategory', 'brand', 'market_price', 'net_quantity')
    search_fields = ('product_name',)
    list_filter = ('category', 'subcategory', 'brand')

@admin.register(FamilyPackage)
class FamilyPackageAdmin(admin.ModelAdmin):
    list_display = ('package_name', 'family_size_min', 'family_size_max', 'base_price')
    search_fields = ('package_name',)

@admin.register(PackageItem)
class PackageItemAdmin(admin.ModelAdmin):
    list_display = ('package', 'product', 'quantity')
    search_fields = ('package__package_name', 'product__product_name')
    list_filter = ('package',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'image', 'pan_no', 'pan_image', 'address', 'contact_no')
    search_fields = ('name', 'pan_no', 'contact_no')
    list_filter = ('name', 'contact_no')

@admin.register(SupplierProduct)
class SupplierProductAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'supply_price')
    search_fields = ('supplier__name', 'product__product_name')
    list_filter = ('supplier',)