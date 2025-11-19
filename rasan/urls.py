from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubCategoryViewSet, BrandViewSet, ProductViewSet, FamilyPackageViewSet, PackageItemViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)
router.register(r'family-packages', FamilyPackageViewSet)
router.register(r'package-items', PackageItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
