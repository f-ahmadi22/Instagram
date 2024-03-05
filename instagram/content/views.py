from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Story
from .serializers import PostSerializer, MentionSerializer, StorySerializer
from log.signals import post_viewed
from log.models import PostView, StoryView
# Create your views here.


class CreatePostAPIView(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MentionUserAPIView(APIView):
    def post(self, request):
        serializer = MentionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowedUsersPostsAPIView(APIView):
    def get(self, request):
        followed_users = request.user.get_followings()
        posts = Post.objects.filter(user__in=followed_users)
        serializer = PostSerializer(posts, many=True)

        # Trigger post_viewed signal for each post
        for post in posts:
            postview = PostView.objects.create(post=post, user=request.user)
            postview.save()
            post_viewed.send(sender=PostView, instance=postview, user=request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class StoryAPIView(APIView):
    def get(self, request):
        story = Story.objects.get(id=request.data['story_id'])
        serializer = StorySerializer(story)

        storyview = StoryView.objects.create(story=story, user=request.user)
        storyview.save()
        post_viewed.send(sender=StoryView, instance=storyview, user=request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)
