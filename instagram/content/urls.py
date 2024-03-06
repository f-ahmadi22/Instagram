from django.urls import path, include
from rest_framework import routers
from .views import CreatePostAPIView, FollowedUsersPostsAPIView, MentionUserAPIView, StoryAPIView, CreateStoryAPIView

urlpatterns = [
    path('create-post/', CreatePostAPIView.as_view(), name='create-post'),  # Create post api
    path('posts/', FollowedUsersPostsAPIView.as_view(), name='posts'),  # Get post of followed users api
    path('mention/', MentionUserAPIView.as_view(), name='mention'),  # Mention someone in a story api
    path('story/<int:pk>/', StoryAPIView.as_view(), name='story'),  # View someone's story api
    path('create-story/', CreateStoryAPIView.as_view(), name='create-story'),  # Create story api
]
