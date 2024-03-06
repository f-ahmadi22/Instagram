from django.urls import path, include
from rest_framework import routers
from .views import (SignupAPIView, LoginAPIView, EditProfileAPIView, ViewProfileAPIView, FollowRequestAPIView,
                    FollowAcceptAPIView, FollowRejectAPIView, UnfollowAPIView)

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),  # User sign up api
    path('login/', LoginAPIView.as_view(), name='login'),   # User login api
    path('edit-profile/', EditProfileAPIView.as_view(), name='edit-profile'),  # Edit profile api
    path('view-profile/<int:pk>/', ViewProfileAPIView.as_view(), name='view-profile'),  # View someone's Profile
    path('follow-request-send/', FollowRequestAPIView.as_view(), name='follow request send'),  # Send follow request
    path('follow-request-accept/', FollowAcceptAPIView.as_view(), name='follow request accept'),  # accept request
    path('follow-request-reject/', FollowRejectAPIView.as_view(), name='follow request reject'),  # reject request
    path('unfollow/', UnfollowAPIView.as_view(), name='unfollow')  # Unfollow a user
]
