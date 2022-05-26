from django.contrib import admin
from resender.models import Chat, MyChat, BlackWord, WhiteWord, Message
from django.contrib.admin import RelatedFieldListFilter


@admin.register(MyChat)
class MyChatAdmin(admin.ModelAdmin):
    list_display = ('name', 'chat_id')
    search_fields = ['name', 'chat_id']


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('name', 'chat_id')
    search_fields = ['name', 'chat_id']


@admin.register(BlackWord)
class BlackWordAdmin(admin.ModelAdmin):
    list_display = ('chat', 'word')
    search_fields = ['chat', 'word']
    list_filter = ['chat__name']


@admin.register(WhiteWord)
class WhiteWordAdmin(admin.ModelAdmin):
    list_display = ('chat', 'my_chat', 'word')
    list_filter = ['chat__name', 'my_chat__name']
    search_fields = ['chat', 'word']


@admin.register(Message)
class MessagedAdmin(admin.ModelAdmin):
    list_filter = ['chat__name', 'date']
    list_display = ('chat', 'date')
    search_fields = ['chat', 'date']

@admin.register(Dialog)
class DialogAdmin(admin.ModelAdmin):
    pass
