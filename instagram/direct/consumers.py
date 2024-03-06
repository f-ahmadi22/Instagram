# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import DialogsModel, MessageModel
from user.models import MyUser


@database_sync_to_async
def get_user_by_pk(pk):
    # Get user by pk instead of token authentication because I don't have front now
    return MyUser.objects.get(pk=pk)


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.dialog_id = None

    async def connect(self):
        pk = self.scope['url_route'].get('kwargs', {}).get('pk')  # Get user pk from url
        self.user = await get_user_by_pk(pk)  # Find user by pk
        self.dialog_id = self.scope['url_route'].get('kwargs', {}).get('dialog_id')  # Get dialog id from url
        self.room_group_name = f'chat_{self.dialog_id}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()  # Connect to websocket

    async def disconnect(self, close_code):  # Close websocket connection
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):  # Handle recieve message
        text_data_json = json.loads(text_data)  # Parse text data

        message = text_data_json['message']

        await self.save_message(message)  # Save message recieved

        # Send message to room group
        await self.channel_layer.group_send(  # Send message in group
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    @database_sync_to_async
    def save_message(self, message_text):
        # Get recipient from dialog
        dialog = DialogsModel.objects.get(id=self.dialog_id)
        if self.user == dialog.user1:
            recipient = dialog.user2
        else:
            recipient = dialog.user1

        # Save message
        message = MessageModel(sender=self.user, recipient=recipient, text=message_text)
        message.save()
