from django.urls import path, include
from rest_framework import routers
from .views import SignupAPIView, LoginAPIView

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
