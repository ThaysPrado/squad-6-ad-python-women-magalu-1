from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .forms import UserModelForm

from .models import Log, Origin, Environment, Level
from .serializers import (LogSerializer, 
                          OriginSerializer, 
                          UserSerializer, 
                          EnvironmentSerializer,
                          LevelSerializer)
from .api_permissions import OnlyAdminCanList

class LogApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Log.objects.all()
    serializer_class = LogSerializer

class OriginApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Origin.objects.all()
    serializer_class = OriginSerializer

class LevelApiViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class EnvironmentListOnlyApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        queryset = Environment.objects.all()
        serializer = EnvironmentSerializer(queryset, many=True)
        return Response(serializer.data)

class UserApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, OnlyAdminCanList]

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserToken(APIView):

    def post(self, request):

        email = request['email']
        password = request['senha']
        
        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'},
                            status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=email, password=password)
        
        if not user:
            return Response({'error': 'Invalid Credentials'}, 
                            status=status.HTTP_404_NOT_FOUND)
        
        token, _ = Token.objects.get_or_create(user=user)
       
        return Response({'token': token.key}, status=status.HTTP_200_OK)

    def user_login(request):
        if  request.method == 'POST':

            response = UserToken.post(request.POST, request.POST)
            status = response.status_code

            if (status != 200):
                return render(request, 'registration/login.html', {'error': response.data['error']})
            else:
                return redirect('/logs', {'token': response.data['token']})
        else:
            form = UserModelForm()

        context = {
            'form': form
        }
        return render(request, 'registration/login.html', {'form': form})
