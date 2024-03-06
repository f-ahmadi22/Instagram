from django.urls import path, include
from rest_framework import routers
from .views import SignupAPIView, LoginAPIView, EditProfileAPIView, ViewProfileAPIView, FollowAPIView, UnfollowAPIView

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),  # User sign up api
    path('login/', LoginAPIView.as_view(), name='login'),   # User login api
    path('edit-profile/', EditProfileAPIView.as_view(), name='edit-profile'),  # Edit profile api
    path('view-profile/<int:pk>/', ViewProfileAPIView.as_view(), name='view-profile'),  # View someone's Profile
    path('follow/', FollowAPIView.as_view(), name='follow'),  # Follow a user
    path('unfollow/', UnfollowAPIView.as_view(), name='unfollow')  # Unfollow a user
]
