from django.shortcuts import render
from .serializers import *
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    """
    自定义得到token username: 账号或者密码 password: 密码或者验证码
    """
    serializer_class = MyTokenObtainPairSerializer


class MyTokenRefreshView(TokenViewBase):
    """
    自定义刷新token refresh: 刷新token的元素
    """
    serializer_class = TokenRefreshSerializer


