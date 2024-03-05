# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import DialogsModel, MessageModel
from user.models import MyUser


@database_sync_to_async
def get_user_by_pk(pk):
    return MyUser.objects.get(pk=pk)


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.dialog_id = None

    async def connect(self):
        pk = self.scope['url_route'].get('kwargs', {}).get('pk')
        self.user = await get_user_by_pk(pk)
        self.dialog_id = self.scope['url_route'].get('kwargs', {}).get('dialog_id')
        self.room_group_name = f'chat_{self.dialog_id}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('111111111111')
        await self.save_message(message)
        print('2222222222222')
        # Send message to room group
        await self.channel_layer.group_send(
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
