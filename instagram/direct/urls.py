# urls.py
from django.urls import path, include
from django.urls import re_path
from .consumers import ChatConsumer
from .views import DialogsModelList
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from instagram.asgi import get_asgi_application

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<pk>\d+)/(?P<dialog_id>\w+)/$', ChatConsumer.as_asgi()),
]

urlpatterns = [
    path('dialogs/', DialogsModelList.as_view(), name='dialogs_list'),

] + websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
