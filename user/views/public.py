from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import generics, status
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.response_wrapper import ResponseWrapper

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q


from django.contrib.auth import get_user_model

User = get_user_model()
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import Group, Permission
from utils.permissions import CheckCustomPermission
# import re
from user.serializers import LoginSerializer
from utils.response_wrapper import ResponseWrapper
from utils.custom_viewset import CustomViewSet
from rest_framework.permissions import AllowAny


# Create your views here.


class LoginViewSet(CustomViewSet):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            username = request.data.get('username', None)
            password = request.data.get('password', None)

            user_qs = User.objects.filter(Q(email=username)|
                                          Q(username= username)).first()
            if user_qs:
                if user_qs.check_password(password):
                    return ResponseWrapper(
                        data=LoginSerializer(user_qs).data,
                        status=200,
                        msg="Success"
                    )
                else:
                    return ResponseWrapper(
                        error_msg="Email or password is incorrect",
                        status=400,
                    )
            else:
                return ResponseWrapper(
                    status=status.HTTP_400_BAD_REQUEST,
                    error_msg="User not found"
                )
        except Exception as e:
            print(e)
            return ResponseWrapper(
                status=status.HTTP_400_BAD_REQUEST,
                error_msg="Something went wrong",
                data=None,
            )
