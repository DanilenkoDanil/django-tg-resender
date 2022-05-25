from django.core.management.base import BaseCommand
from telethon.sync import TelegramClient
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


def main():
    client = TelegramClient(
        "session_for_id",
        2547559,
        "1a1975ef3b460f054d2777ddf45e8faf"
    )
    client.start()
    client.disconnect()


class Command(BaseCommand):
    help = 'Создание сессии'

    def handle(self, *args, **options):
        main()
