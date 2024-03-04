from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'comments', views.CommentViewSet)
router.register(r'like-posts', views.LikePostViewSet)
router.register(r'like-comments', views.LikeCommentViewSet)
router.register(r'like-stories', views.LikeStoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]