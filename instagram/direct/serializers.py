from rest_framework import serializers
from .models import DialogsModel


class DialogSerializer(serializers.ModelSerializer):

    class Meta:
        model = DialogsModel
        fields = ['id', 'user1', 'user2']

