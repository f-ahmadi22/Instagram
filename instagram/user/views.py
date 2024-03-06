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
from log.models import ProfileView


class SignupAPIView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)  # Serialize input data
        if serializer.is_valid(): # If serializer is vallid
            user = serializer.save()  # Create User
            refresh = RefreshToken.for_user(user)  # Generate token
            # Return refresh and access token of user
            return Response({'message': 'User created successfully', 'refresh': str(refresh),
                             'access': str(refresh.access_token)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return Serializer errors


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
    # Authentication needed
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = UserProfileSerializer(user, data=request.data, partial=True)  # Serialize data fields updated
        if serializer.is_valid():
            serializer.save()  # Save new data to user
            return Response({'message': 'Profile updated successfully'})  # Profile edited successfully
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Invalid data errors


class ViewProfileAPIView(APIView):
    def get(self, request, pk):
        user = MyUser.objects.filter(pk=pk).first()  # Get user by pk
        if user:
            if user.is_private:  # If user is private
                # If the user is my following so I can see his profile as a public
                if UserRelationship.objects.filter(follower=request.user).exists():
                    # Serialize data as a public user
                    serializer = UserProfilePublicSerializer(user)
                    # Create profile view
                    profile = ProfileView.objects.create(user=request.user, user_profile=user)
                    profile.save()
                    # Send signal of viewing someone's profile to add user's view_count
                    post_viewed.send(sender=ProfileView, instance=profile, user=request.user)
                    # Return user's profile
                    return Response(serializer.data)

                else:  # If user is private and not my following
                    # Create profile view
                    profile = ProfileView.objects.create(user=request.user, user_profile=user)
                    profile.save()
                    # Send signal of viewing someone's profile to add user's view_count
                    post_viewed.send(sender=ProfileView, instance=profile, user=request.user)
                    serializer = UserProfilePrivateSerializer(user)
                    # Return user's profile
                    return Response(serializer.data)
            else:  # If user is public
                # Create profile view
                profile = ProfileView.objects.create(user=request.user, user_profile=user)
                profile.save()
                # Send signal of viewing someone's profile to add user's view_count
                post_viewed.send(sender=ProfileView, instance=profile, user=request.user)
                serializer = UserProfilePublicSerializer(user)
                # Return user's profile
                return Response(serializer.data)

        # User not found error, wrong pk passed
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class FollowAPIView(APIView):
    # Authentication needed
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Find the user by pk to follow
        user_to_follow = get_object_or_404(MyUser, pk=request.data['user'])
        if user_to_follow:
            # Follow user and create relation
            relationship, created = UserRelationship.objects.get_or_create(
                follower=request.user,
                following=user_to_follow
            )
            if created:
                # Return success response
                return Response({'message': 'User followed successfully'}, status=status.HTTP_201_CREATED)
            # User already followed
            return Response({'error': 'User already followed'}, status=status.HTTP_400_BAD_REQUEST)
        # User not found, wrong pk passed
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class UnfollowAPIView(APIView):
    # Authentication needed
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Find the user by pk to unfollow
        user_to_unfollow = MyUser.objects.filter(id=request.data['user']).first()
        if user_to_unfollow:
            # Find user relation and delete
            UserRelationship.objects.filter(
                follower=request.user,
                following=user_to_unfollow
            ).delete()
            # Return success response
            return Response({'message': 'User unfollowed successfully'}, status=status.HTTP_201_CREATED)
        # User not found, wrong pk passed
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
