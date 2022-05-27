from rest_framework import status, generics, permissions
from telethon.sync import TelegramClient
from rest_framework.response import Response
import asyncio
import json
from resender.models import Dialog
from resender.serializers import DialogSerializer


class GetIdApiView(generics.ListAPIView):
    queryset = Dialog.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def list(self, request, *args, **kwargs):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        client = TelegramClient(
            "session_for_id",
            3566267,
            "77c8ec3ad6b760c7d247ef4159721524",
            loop=loop
        )
        client.start()
        for dialog in client.iter_dialogs():
            if dialog.is_channel:
                try:
                    Dialog.objects.get(chat_id=str(dialog.id))
                except Dialog.DoesNotExist:
                    Dialog.objects.create(chat_id=str(dialog.id), name=str(dialog.name))
        serializer = DialogSerializer(data=Dialog.objects.all(), many=True)
        serializer.is_valid()
        client.disconnect()
        return Response(serializer.data, status=status.HTTP_200_OK)
