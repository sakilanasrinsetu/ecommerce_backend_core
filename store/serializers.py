from rest_framework import serializers
from base.serializers import BaseModelSerializer
from store.models import  Store, StorePaymentMethod
# from user.serializers import UserSerializer
from locations.serializers import DistrictSerializer
from point_of_sale.serializers import POSUserAreasSerializer, POSUserRegionsSerializer


class StoreSerializer(BaseModelSerializer):
    slug = serializers.CharField(read_only = True)

    class Meta:
        model = Store
        fields = '__all__'


    def to_representation(self, instance):
        self.fields["district"] = DistrictSerializer(read_only=True)
        self.fields["pos_area"] = POSUserAreasSerializer(read_only=True)
        self.fields["region"] = POSUserRegionsSerializer(read_only=True)

        return super(StoreSerializer, self).to_representation(instance)


class StorePaymentMethodSerializer(BaseModelSerializer):

    class Meta:
        model = StorePaymentMethod
        fields = '__all__'


    def to_representation(self, instance):
        self.fields["store"] = StoreSerializer(read_only=True)

        return super(StorePaymentMethodSerializer, self).to_representation(instance)
