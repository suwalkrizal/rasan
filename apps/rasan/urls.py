from .views import *
from django.urls import path

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name = 'category-detail'),

    path('subcategories/', SubCategoryListCreateAPIView.as_view(), name='subcategory-list'),
    path('subcategories/<int:pk>/', SubCategoryDetailAPIView.as_view(), name= 'subcategory-detail'),

    path('brands/', BrandListCreateAPIView.as_view(), name='brand-list'),
    path('brands/<int:pk>/', BrandDetailAPIView.as_view(), name= 'brand-detail'),

    path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name= 'product-detail'),

    path('familypackages/', FamilyPackageListCreateAPIView.as_view(), name='familypackage-list'),
    path('familypackages/<int:pk>/', FamilyPackageDetailAPIView.as_view(), name= 'familypackage-detail'),
    
    path('packageitems/', PackageItemListCreateAPIView.as_view(), name='packageitem-list'),
    path('packageitems/<int:pk>/', PackageItemDetailAPIView.as_view(), name= 'packageitem-detail'),

    path('suppliers/', SupplierListCreateAPIView.as_view(), name='supplier-list'),
    path('suppliers/<int:pk>/', SupplierDetailAPIView.as_view(), name= 'supplier-detail'),

    path('supplierproducts/', SupplierProductListCreateAPIView.as_view(), name='supplierproduct-list'),
    path('supplierproducts/<int:pk>/', SupplierProductDetailAPIView.as_view(), name= 'supplierproduct-detail'),
]
