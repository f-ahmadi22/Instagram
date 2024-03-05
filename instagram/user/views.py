from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .models import MyUser, UserRelationship
from .serializers import (SignupSerializer, UserProfilePrivateSerializer, UserProfilePublicSerializer,
                          LoginSerializer, UserProfileSerializer)
from log.signals import post_viewed


class SignupAPIView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)  # Serialize input data
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


class EditProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        print(request)
        user = request.user
        print(user)
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Profile updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewProfileAPIView(APIView):
    def get(self, request, pk):
        user = MyUser.objects.filter(pk=pk).first()
        if user:
            if user.is_private:
                if UserRelationship.objects.filter(follower=request.user).exists():
                    serializer = UserProfilePublicSerializer(user)
                    post_viewed.send(sender=MyUser, instance=user, user=request.user)
                    return Response(serializer.data)
                else:
                    post_viewed.send(sender=MyUser, instance=user, user=request.user)
                    serializer = UserProfilePrivateSerializer(user)
                    return Response(serializer.data)
            else:
                post_viewed.send(sender=MyUser, instance=user, user=request.user)
                serializer = UserProfilePublicSerializer(user)
                return Response(serializer.data)

        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class FollowAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user_to_follow = get_object_or_404(MyUser, pk=request.data['user'])
        if user_to_follow:
            relationship, created = UserRelationship.objects.get_or_create(
                follower=request.user,
                following=user_to_follow
            )
            if created:
                return Response({'message': 'User followed successfully'}, status=status.HTTP_201_CREATED)
            return Response({'error': 'User already followed'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class UnfollowAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user_to_unfollow = MyUser.objects.filter(id=request.data['user']).first()
        if user_to_unfollow:
            UserRelationship.objects.filter(
                follower=request.user,
                following=user_to_unfollow
            ).delete()
            return Response({'message': 'User unfollowed successfully'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
