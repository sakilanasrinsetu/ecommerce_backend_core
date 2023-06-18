from blogs.serializers import BlogSerializer
from blogs.models import Blog
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from utils.custom_viewset import CustomViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from utils.response_wrapper import ResponseWrapper
from discount.models import Discount
from discount.serializers import DiscountSerializer

from datetime import date, datetime, timedelta
from django.utils import timezone
from django.db.models import Q


class PublicDiscountViewSet(CustomViewSet):
    queryset = Discount.objects.filter(is_active = True)
    serializer_class = DiscountSerializer
    lookup_field = "pk"

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())

        today = datetime.strptime(
                str(timezone.datetime.now().date()) + " 00:00:00", '%Y-%m-%d %H:%M:%S'
            )
        current_time = timezone.datetime.now().time()


        qs = qs.filter(Q(start_date__lte=today, end_date__gte=today, discount_schedule_type = 'date_wise')| Q(start_time__lte= current_time, end_time__gte=current_time, discount_schedule_type = 'time_wise'))

        serializer_class = self.get_serializer_class()


        page_qs = self.paginate_queryset(qs)
        serializer = serializer_class(instance=page_qs, many=True)

        paginated_data = self.get_paginated_response(serializer.data)
        return ResponseWrapper(data=paginated_data.data, msg="Success", status=200)

