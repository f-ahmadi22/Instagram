from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CommentAPIView, LikePostAPIView, LikeStoryAPIView, LikeCommentAPIView

urlpatterns = [
    path('comments/', CommentAPIView.as_view(), name='comments'),  # Post and delete Comment api
    path('like-post/', LikePostAPIView.as_view(), name='like-post'),  # Like a post api
    path('like-story/', LikeStoryAPIView.as_view(), name='like-story'),  # Like a story api
    path('like-comment/', LikeCommentAPIView.as_view(), name='like-comment')  # Like a comment api
]
