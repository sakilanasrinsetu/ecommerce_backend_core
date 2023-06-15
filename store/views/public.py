from store.serializers import StoreSerializer
from store.models import District, Store
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import  AllowAny
# from store.filters import StoreFilter
from rest_framework.views import APIView
from utils.response_wrapper import ResponseWrapper
from utils.custom_viewset import CustomViewSet
from store.filters import StoreFilter



class PublicStoreViewset(CustomViewSet):
    permission_classes =  (AllowAny,)
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    lookup_field = "pk"

    filterset_class = StoreFilter

