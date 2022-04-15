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
        3566267,
        "77c8ec3ad6b760c7d247ef4159721524"
    )
    client.start()
    client.disconnect()


class Command(BaseCommand):
    help = 'Создание сессии'

    def handle(self, *args, **options):
        main()
