from catalog.serializers import ProductGroupWithCategoriesSerializer
from catalog.models import ProductGroup, Category, ProductBrand, TaxCategory
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from utils.custom_viewset import CustomViewSet
from rest_framework.permissions import IsAuthenticated
from utils.response_wrapper import ResponseWrapper
from django.db.models import  Prefetch, F, Sum
from catalog.serializers import CategorySerializer


class PublicProductGroupViewSet(CustomViewSet):
    queryset = ProductGroup.objects.filter(show_in_ecommerce=True, is_active=True).order_by('ordering').prefetch_related(
        Prefetch('categories', queryset=Category.objects.filter(show_in_ecommerce=True, is_active=True))
    )
    serializer_class = ProductGroupWithCategoriesSerializer
    lookup_field = "pk"


class PublicCategoryViewSet(CustomViewSet):
    queryset = Category.objects.filter(show_in_ecommerce=True, is_active=True, status= "child").order_by('ordering').prefetch_related(
        Prefetch('categories', queryset=Category.objects.filter(show_in_ecommerce=True, is_active=True))
    )
    serializer_class = CategorySerializer
    lookup_field = "pk"