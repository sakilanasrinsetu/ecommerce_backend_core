from discount.serializers import DiscountSerializer
from discount.models import Discount
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from utils.custom_viewset import CustomViewSet
from rest_framework.permissions import IsAuthenticated
from utils.response_wrapper import ResponseWrapper
from datetime import date, datetime, timedelta
from django.utils import timezone
from utils.actions import send_action
from discount.filters import DiscountFilter



class AdminDiscountViewSet(CustomViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    lookup_field = "pk"
    filterset_class = DiscountFilter
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if not serializer.is_valid():
            return ResponseWrapper(
                error_msg=serializer.errors,
                error_code=400,
                status=400)
        
        start_date = serializer.validated_data.get('start_date')
        end_date = serializer.validated_data.get('end_date')
        start_time = serializer.validated_data.get('start_time')
        end_time = serializer.validated_data.get('end_time')
        discount_schedule_type = serializer.validated_data.get('discount_schedule_type')
        discount_type = serializer.validated_data.get('discount_type')
        amount = serializer.validated_data.get('amount')

        is_active = False
        
        today = datetime.strptime(
                str(timezone.datetime.now().date()) + " 00:00:00", '%Y-%m-%d %H:%M:%S'
            )
        current_time = timezone.datetime.now().time()

        if discount_type == 'percentage' and amount > 100:
            return ResponseWrapper(
                    error_msg='Discount Amount Must Be Less Than 100',
                    error_code=406, status=406
                )


        if discount_schedule_type == 'date_wise':
            if not start_date:
                return ResponseWrapper(
                    error_msg='Start Date is Required',
                    error_code=406, status=406
                )
            
            if not end_date:
                return ResponseWrapper(
                    error_msg='End Date is Required',
                    error_code=406, status=406
                )

            if start_date.date() > end_date.date():
                return ResponseWrapper(
                    error_msg='Start Date Must Be Less Than End Date',
                    error_code=406, status=406
                )
            
            if start_date.date() <= today.date() and end_date.date() >= today.date():
                is_active = True
            
        elif discount_schedule_type == 'time_wise':
            if not start_time:
                return ResponseWrapper(
                    error_msg='Start Time is Required',
                    error_code=406, status=406
                )
            
            if not end_time:
                return ResponseWrapper(
                    error_msg='End Time is Required',
                    error_code=406, status=406
                )
            

            if start_time > end_time:
                return ResponseWrapper(
                    error_msg='Start Time Must Be Less Than End Time',
                    error_code=406, status=406
                )
            if start_time <= current_time and end_time >= current_time:
                is_active = True

        qs = serializer.save(is_active = is_active)
        

        # Save Logger for Tracking 

        request_method = request.method
        request_url = request.build_absolute_uri()
        request_data = request.data 
        response_data = serializer.data

        try:
            send_action(qs, request_method, request_url,request_data, response_data)
        except:
            pass
        
        return ResponseWrapper(data=serializer.data,
                            msg='Success', status=200)
    
    def update(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, partial=True)

        if not serializer.is_valid():
            return ResponseWrapper(
                error_msg=serializer.errors,
                error_code=400,
                status=400)
        
        print('ddddddddd', kwargs["pk"])
        
        discount_qs = self.queryset.filter(id = kwargs["pk"]).last()
        print('ddddddddddd', discount_qs)
        if not discount_qs:
            return ResponseWrapper(
                error_code=404,
                error_msg='Discount Not Found',
                status=404)
        
        start_date = serializer.validated_data.get('start_date', discount_qs.start_date)
        end_date = serializer.validated_data.get('end_date', discount_qs.end_date)
        start_time = serializer.validated_data.get('start_time', discount_qs.start_time)
        end_time = serializer.validated_data.get('end_time', discount_qs.end_time)
        discount_schedule_type = serializer.validated_data.get('discount_schedule_type', discount_qs.discount_schedule_type)
        discount_type = serializer.validated_data.get('discount_type', discount_qs.discount_type)
        amount = serializer.validated_data.get('amount', discount_qs.amount)

        is_active = False
        
        today = datetime.strptime(
                str(timezone.datetime.now().date()) + " 00:00:00", '%Y-%m-%d %H:%M:%S'
            )
        current_time = timezone.datetime.now().time()

        if discount_type == 'percentage' and amount > 100:
            return ResponseWrapper(
                    error_msg=f'Discount Amount Must Be Less Than 100, Here Discount Amount is {amount}',
                    error_code=406, status=406
                )


        if discount_schedule_type == 'date_wise':
            if not start_date:
                return ResponseWrapper(
                    error_msg='Start Date is Required',
                    error_code=406, status=406
                )
            
            if not end_date:
                return ResponseWrapper(
                    error_msg='End Date is Required',
                    error_code=406, status=406
                )

            if start_date.date() > end_date.date():
                return ResponseWrapper(
                    error_msg='Start Date Must Be Less Than End Date',
                    error_code=406, status=406
                )
            
            if start_date.date() <= today.date() and end_date.date() >= today.date():
                is_active = True
            
        elif discount_schedule_type == 'time_wise':
            if not start_time:
                return ResponseWrapper(
                    error_msg='Start Time is Required',
                    error_code=406, status=406
                )
            
            if not end_time:
                return ResponseWrapper(
                    error_msg='End Time is Required',
                    error_code=406, status=406
                )
            

            if start_time > end_time:
                return ResponseWrapper(
                    error_msg='Start Time Must Be Less Than End Time',
                    error_code=406, status=406
                )
            if start_time <= current_time and end_time >= current_time:
                is_active = True

        qs = serializer.update(instance=qs, validated_data=serializer.validated_data)

        serializer = self.serializer_class(instance=qs)


        # Save Logger for Tracking 

        request_method = request.method
        request_url = request.build_absolute_uri()
        request_data = request.data 
        response_data = serializer.data

        try:
            send_action(qs, request_method, request_url,request_data, response_data)
        except:
            pass
        
        return ResponseWrapper(data=serializer.data, msg='Success', status=200)
