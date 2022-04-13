from django.core.management.base import BaseCommand
from telethon.sync import TelegramClient
from resender.models import BlackWord, WhiteWord, Chat, MyChat, Message
from telethon import events
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


def main():
    client = TelegramClient(
        "session",
        3566267,
        "77c8ec3ad6b760c7d247ef4159721524"
    )
    client.start()
    client.get_dialogs()

    my_chats_objects = MyChat.objects.all()
    my_chats_list = []
    my_chats_entity = []
    for i in my_chats_objects:
        my_chats_list.append(str(i.chat_id))
    for dialog in client.iter_dialogs():
        if dialog.is_channel:
            print(f'{dialog.id}:{dialog.title}')
            if str(dialog.id) in my_chats_list:
                my_chats_entity.append(dialog)

    @client.on(events.NewMessage())
    async def handler_first(event):
        chats_list = []
        chat_objects = Chat.objects.all()
        for i in chat_objects:
            chats_list.append(str(i.chat_id).replace("-100", ""))
        try:
            if str(event.message.peer_id.channel_id) in chats_list:
                chat = Chat.objects.get(chat_id="-100" + str(event.message.peer_id.channel_id))
                black_words = []
                white_words = []
                black_words_objects = BlackWord.objects.filter(chat=chat)
                white_words_objects = WhiteWord.objects.filter(chat=chat)
                for i in black_words_objects:
                    black_words.append(i.word)
                for i in white_words_objects:
                    white_words.append(i.word)
                if all(item.lower() in event.message.text.lower() for item in white_words) and \
                        not any(item.lower() in event.message.text.lower() for item in black_words):
                    print(event.message.text)
                    Message.objects.create(chat=chat, message=event.message.text)
                    for target in my_chats_entity:
                        try:
                            await client.forward_messages(target, event.message)
                        except Exception as e:
                            print(e)
                            await client.send_message(target, chat.name)
                            await client.send_message(target, event.message.text)
                print('Новое сообщение')
        except AttributeError:
            print('AttributeError')
    client.run_until_disconnected()


class Command(BaseCommand):
    help = 'Запуск бота'

    def handle(self, *args, **options):
        main()
