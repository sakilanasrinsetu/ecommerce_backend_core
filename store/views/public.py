from store.serializers import DistrictSerializer
from store.models import District, Store
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import  AllowAny
# from store.filters import StoreFilter
from rest_framework.views import APIView
from utils.response_wrapper import ResponseWrapper
from utils.custom_viewset import CustomViewSet



class PublicDistrictViewset(CustomViewSet):
    permission_classes =  (AllowAny,)
    serializer_class = DistrictSerializer
    queryset = District.objects.all()
    search_fields = ['name']
    lookup_field = "pk"


# class PublicStoreListAPIView(ListAPIView):
#     permission_classes =  (AllowAny,)
#     serializer_class = PublicStoreLiteSerializer
#     queryset = Store.objects.select_related('district', 'created_by', 'updated_by').filter()
#     search_fields = ['district__name', 'name']
#     filterset_class = StoreFilter

# class PublicStoreRetrieveAPIView(RetrieveAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = PublicStoreSerializer
#     queryset = Store.objects.select_related('district', 'created_by', 'updated_by').filter()
#     lookup_field = 'slug'



# class getAllStoreList(APIView):
#     permission_classes = (AllowAny,)

#     def get(self, request, format=None):
#         query_set =Store.objects.all()
#         serializer = StoreLiteSerializer(query_set, many=True)
#         return Response(serializer.data)
