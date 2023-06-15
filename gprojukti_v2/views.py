from utils.response_wrapper import ResponseWrapper
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from utils.custom_viewset import CustomViewSet
from utils.response_wrapper import ResponseWrapper


class HealthCheckViewset(CustomViewSet):
    permission_classes =  (AllowAny,)
    serializer_class = None
    queryset = None
    lookup_field = None


    def health_check(self, request):
        data = {
            'message': 'GProjukti Version 2 API Service',
            'method': request.method
        }
        return ResponseWrapper(data=data, status=200, msg="Success")