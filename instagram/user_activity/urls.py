from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CommentAPIView, LikePostAPIView, LikeStoryAPIView, LikeCommentAPIView

urlpatterns = [
    path('comments/', CommentAPIView.as_view(), name='comments'),
    path('like-post/', LikePostAPIView.as_view(), name='like-post'),
    path('like-story/', LikeStoryAPIView.as_view(), name='like-story'),
    path('like-comment/', LikeCommentAPIView.as_view(), name='like-comment')
]
