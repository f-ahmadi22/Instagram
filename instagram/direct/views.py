from django.shortcuts import render
from rest_framework.views import APIView
from .models import DialogsModel
from django.db.models import Q
from .serializers import DialogSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class DialogsModelList(APIView):

    model = DialogsModel

    def get(self, request):
        user = request.user
        qs = DialogsModel.objects.filter(Q(user1_id=user.id) | Q(user2_id=user.id)) \
            .select_related('user1', 'user2')
        qs = qs.order_by('-created')
        serializer = DialogSerializer(qs, context={'user_pk': user.id}, many=True)
        return Response({'dialogs': serializer.data}, status=status.HTTP_200_OK)
