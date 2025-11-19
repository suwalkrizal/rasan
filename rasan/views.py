from django.shortcuts import render
from .models import Category, SubCategory, Brand, Product, FamilyPackage, PackageItem
from .serializers import *
from rest_framework import viewsets, permissions

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FamilyPackageViewSet(viewsets.ModelViewSet):
    queryset = FamilyPackage.objects.all()
    serializer_class = FamilyPackageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PackageItemViewSet(viewsets.ModelViewSet):
    queryset = PackageItem.objects.all()
    serializer_class = PackageItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]