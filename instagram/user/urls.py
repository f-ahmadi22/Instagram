from django.urls import path, include
from rest_framework import routers
from .views import SignupAPIView, LoginAPIView, EditProfileAPIView, ViewProfileAPIView

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('edit-profile/', EditProfileAPIView.as_view(), name='edit-profile'),
    path('view-profile/<int:pk>/', ViewProfileAPIView.as_view(), name='view-profile'),
]
