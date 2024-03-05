from django.urls import path, include
from rest_framework import routers
from .views import CreatePostAPIView, FollowedUsersPostsAPIView, MentionUserAPIView, StoryAPIView, CreateStoryAPIView

urlpatterns = [
    path('create-post/', CreatePostAPIView.as_view(), name='create-post'),
    path('posts/', FollowedUsersPostsAPIView.as_view(), name='posts'),
    path('mention/', MentionUserAPIView.as_view(), name='mention'),
    path('story/<int:pk>/', StoryAPIView.as_view(), name='story'),
    path('create-story/', CreateStoryAPIView.as_view(), name='create-story'),
]
