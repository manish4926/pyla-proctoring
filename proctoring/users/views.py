from app.controller.user.UserController import UserController
import app.core.Core as Core
import app.libraries.Auth as Auth
from app.core import Response
import json
import jwt

from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated


from app import core
from users.serializer import LoginSerializer
from django.contrib.auth import authenticate

from datetime import datetime, timedelta

from django.conf import settings
from app.core.Model import Model
from app.model import Stocks as STOCKS, Stocks

@api_view(['POST'])
@permission_classes([])
def login(request):
    try:
        data = request.data

        serializer = LoginSerializer(data=request.data)
        #TODO create login history
        if serializer.is_valid():
            user = serializer.validated_data['user']
            # Generate JWT tokens (access and refresh)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # token = Token.objects.create()
            #TODO create entry for token and check in middleware whether token exist or not

            return Response.jsonTokenResponse({
                'token_type': 'Bearer',
                'expires_in': Core.get_env('TOKEN_EXPIRY'),
                'refresh_token': str(refresh),
                'access_token': access_token
            })

        return Response.error("Invalid Login ID Or Password")
    except Exception as e:
        return Response.error(str(e))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getLoginData(request):
    try:
        auth = Auth.Login.getUserByToken(request)
        return Response.success(auth.getData())
    except Exception as e:
        return Response.error(str(e))


