from channels.testing import WebsocketCommunicator
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from django.test import TestCase
from django.urls import reverse

import direct.urls
from .consumers import ChatConsumer
from .models import DialogsModel, MessageModel
from user.models import MyUser
import asyncio
import websockets
import json


class ChatConsumerTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = MyUser.objects.create_user(username='user1', email='user1@example.com')
        cls.user2 = MyUser.objects.create_user(username='user2', email='user2@example.com')

    def setUp(self):
        self.dialog = DialogsModel.objects.create(user1=self.user1, user2=self.user2)

    async def connect_to_websocket(self):
        uri = f"ws://localhost:8000/ws/chat/{self.user1.pk}/{self.dialog.id}"  # Replace with your WebSocket URI
        async with websockets.connect(uri) as websocket:
            await websocket.send("Hello, WebSocket!")
            response = await websocket.recv()
            print("Received:", response)

        # Run the async function in an event loop
    asyncio.get_event_loop().run_until_complete(connect_to_websocket())

