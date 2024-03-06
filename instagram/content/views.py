from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Story
from .serializers import PostSerializer, MentionSerializer, StorySerializer
from log.signals import post_viewed
from log.models import PostView, StoryView
# Create your views here.


class CreatePostAPIView(APIView):  # Create post
    def post(self, request):
        serializer = PostSerializer(data=request.data)  # Serialize input data
        if serializer.is_valid():  # Return serializer data If data is valid
            serializer.save(user=request.user)  # Create post
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Invalid data


class CreateStoryAPIView(APIView):
    def post(self, request):
        serializer = StorySerializer(data=request.data)  # Serialize input data
        if serializer.is_valid():  # Return serializer data If data is valid
            serializer.save(user=request.user)  # Create story
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Invalid data


class MentionUserAPIView(APIView):
    def post(self, request):
        serializer = MentionSerializer(data=request.data)  # Serialize input data
        if serializer.is_valid():  # Return serializer data If data is valid
            serializer.save(user=request.user)  # Create mention
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Invalid data


class FollowedUsersPostsAPIView(APIView):
    def get(self, request):
        followed_users = request.user.get_followings()  # Get list of followings of user
        posts = Post.objects.filter(user__in=followed_users)  # Filter post of referred users
        serializer = PostSerializer(posts, many=True)  # Serialize filtered data

        # Trigger post_viewed signal for each post
        for post in posts:
            postview = PostView.objects.create(post=post, user=request.user)  # Save postview object
            postview.save()
            post_viewed.send(sender=PostView, instance=postview, user=request.user)  # Send signal after save model

        return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data as output


class StoryAPIView(APIView):
    def get(self, request, pk):
        story = Story.objects.get(pk=pk)  # Find story by pk
        serializer = StorySerializer(story)  # Serialize story object found

        storyview = StoryView.objects.create(story=story, user=request.user)  # Save story view object
        storyview.save()
        post_viewed.send(sender=StoryView, instance=storyview, user=request.user)  # Send signal after save model

        return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data as output


class PostAPIView(APIView):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)  # Find post by pk
        serializer = PostSerializer(post)  # Serialize post object found

        postview = PostView.objects.create(post=post, user=request.user)  # Save post view object
        postview.save()
        post_viewed.send(sender=PostView, instance=postview, user=request.user)  # Send signal after save model

        return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data as output
