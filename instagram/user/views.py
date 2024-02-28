from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, UserRelationship
from .serializers import UserSerializer, UserProfilePrivateSerializer, UserProfilePublicSerializer


class SignupAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)  # Serialize input data
        if serializer.is_valid():
            user = serializer.save()  # Create User
            refresh = RefreshToken.for_user(user)  # Generate token
            return Response({'message': 'User created successfully', 'refresh': str(refresh),
                             'access': str(refresh.access_token)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
