from django.urls import path, include
from rest_framework import routers
from .views import SignupAPIView

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),
]
