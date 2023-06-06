from utils.response_wrapper import ResponseWrapper
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request

@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request: Request) -> ResponseWrapper:
    data = {
        'message': 'GProjukti Version 2 API Service',
        'method': request.method
    }
    return ResponseWrapper(data=data, status=200, msg="Success")