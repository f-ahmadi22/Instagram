# urls.py
from django.urls import path, include
from django.urls import re_path
from . import consumers
from .views import DialogsModelList


urlpatterns = [
    path('dialogs/', DialogsModelList.as_view(), name='dialogs_list'),
    re_path(r'ws/dialog/(?P<dialog_id>\d+)/$', consumers.ChatConsumer.as_asgi()),
]
