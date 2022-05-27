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
    print('Start')
    client = TelegramClient(
        "session",
        2547559,
        "1a1975ef3b460f054d2777ddf45e8faf"
    )
    client.start()
    client.get_dialogs()

    my_chats_objects = MyChat.objects.all()
    my_chats_list = []
    my_chats_entity = {}
    for i in my_chats_objects:
        my_chats_list.append(str(i.chat_id))
    for dialog in client.iter_dialogs():
        if dialog.is_channel:
            if str(dialog.id) in my_chats_list:
                my_chats_entity[str(dialog.id)] = dialog

    @client.on(events.NewMessage())
    async def handler_first(event):
        print('New_message')
        my_chats_send = []
        chats_list = []
        chat_objects = Chat.objects.all()
        for i in chat_objects:
            chats_list.append(str(i.chat_id).replace("-100", ""))
        print()
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
                    white_words.append([i.word, i.id])
                try:
                    if not any(item.lower() in event.message.text.lower() for item in black_words):
                        for word in white_words:
                            if word[0].lower() in event.message.text.lower():
                                object_word = WhiteWord.objects.get(id=word[1])
                                try:
                                    target = my_chats_entity[object_word.my_chat.chat_id]
                                except Exception as e:
                                    continue
                                if object_word.my_chat.chat_id not in my_chats_send:
                                    Message.objects.create(chat=chat, message=event.message.text)
                                    try:
                                        await client.send_message(target, chat.name)
                                        await client.forward_messages(target, event.message)
                                    except Exception as e:
                                        await client.send_message(target, chat.name)
                                        await client.send_message(target, event.message.text)
                                    my_chats_send.append(object_word.my_chat.chat_id)
                except Exception as e:
                    print(e)
        except AttributeError:
            pass
    client.run_until_disconnected()


class Command(BaseCommand):
    help = 'Запуск бота'

    def handle(self, *args, **options):
        main()
