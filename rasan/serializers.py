from .models import Category, SubCategory, Brand, Product, FamilyPackage, PackageItem
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class FamilyPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyPackage
        fields = '__all__'

class PackageItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageItem
        fields = '__all__'
