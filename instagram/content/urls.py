from django.urls import path, include
from rest_framework import routers
from .views import CreatePostAPIView, FollowedUsersPostsAPIView, MentionUserAPIView


urlpatterns = [
    path('create-post/', CreatePostAPIView.as_view(), name='create-post'),
    path('posts/', FollowedUsersPostsAPIView.as_view(), name='posts'),
    path('mention/', MentionUserAPIView.as_view(), name='mention')
]
