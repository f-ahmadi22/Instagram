from rest_framework import serializers
from .models import DialogsModel
from user.serializers import UserProfilePrivateSerializer


class DialogSerializer(serializers.ModelSerializer):
    user1 = UserProfilePrivateSerializer()
    user2 = UserProfilePrivateSerializer()

    class Meta:
        model = DialogsModel
        fields = ['id', 'user1', 'user2']

