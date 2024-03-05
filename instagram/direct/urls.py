# urls.py
from django.urls import path, include
from django.urls import re_path
from .consumers import ChatConsumer
from .views import DialogsModelList
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

websocket_urlpatterns = [
    path('ws/chat/<int:dialog_id>/', ChatConsumer.as_asgi()),
]

urlpatterns = [
    path('dialogs/', DialogsModelList.as_view(), name='dialogs_list'),

] + websocket_urlpatterns

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
