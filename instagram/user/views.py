from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, UserRelationship
from .serializers import UserSerializer, UserProfilePrivateSerializer, UserProfilePublicSerializer, LoginSerializer


class SignupAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)  # Serialize input data
        if serializer.is_valid():
            user = serializer.save()  # Create User
            refresh = RefreshToken.for_user(user)  # Generate token
            return Response({'message': 'User created successfully', 'refresh': str(refresh),
                             'access': str(refresh.access_token)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)  # serialize input data
        if serializer.is_valid():
            user = serializer.validated_data['user']
            if user is None:
                # Invalid data
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

            refresh = RefreshToken.for_user(user)  # Generate token
            # Successful login
            return Response(
                {'message': 'Login successful', 'refresh': str(refresh), 'access': str(refresh.access_token)})
        # Invalid credentials
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
