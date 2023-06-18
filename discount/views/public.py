from blogs.serializers import BlogSerializer
from blogs.models import Blog
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from utils.custom_viewset import CustomViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from utils.response_wrapper import ResponseWrapper
from discount.models import Discount
from discount.serializers import DiscountSerializer


class PublicDiscountViewSet(CustomViewSet):
    queryset = Discount.objects.filter(is_active = True)
    serializer_class = DiscountSerializer
    lookup_field = "pk"
