from django.contrib.auth import get_user_model
from django.db.models import Sum
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from products.models import Product,PreOrderProductForm,TransferProduct
from catalog.models import TaxCategory, ProductBrand
from base.serializers import ReadWriteSerializerMethodField, BaseModelSerializer
from rest_framework.serializers import ModelSerializer

from datetime import date
User = get_user_model()


class ProductSerializer(BaseModelSerializer):
    slug = serializers.CharField(read_only=True)
    translation = serializers.JSONField(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"