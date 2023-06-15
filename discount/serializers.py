# from base.serializers import BaseModelSerializer
from discount.models import Discount
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class DiscountSerializer(serializers.ModelField):
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Discount
        fields = "__all__"
