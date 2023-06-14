from rest_framework import serializers
from base.serializers import BaseModelSerializer
from store.models import District, Store, StorePaymentMethod
# from user.serializers import UserSerializer


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = '__all__'
