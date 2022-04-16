from django.db import models


class MyChat(models.Model):
    name = models.CharField(max_length=200)
    chat_id = models.CharField(max_length=200)

    def __str__(self):
        return f'#{self.name}'

    class Meta:
        verbose_name = 'Канал для пересылки'
        verbose_name_plural = 'Каналы для пересылки'


class Chat(models.Model):
    name = models.CharField(max_length=200)
    chat_id = models.CharField(max_length=200)

    def __str__(self):
        return f'#{self.name}'

    class Meta:
        verbose_name = 'Чат откуда парсить'
        verbose_name_plural = 'Чаты откуда парсить'


class WhiteWord(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    my_chat = models.ForeignKey(MyChat, on_delete=models.CASCADE, blank=True, null=True)
    word = models.CharField(max_length=200)

    def __str__(self):
        return f'#{self.word} для {self.chat}'

    class Meta:
        verbose_name = 'Ключевое слово'
        verbose_name_plural = 'Ключевые слова'


class BlackWord(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)

    def __str__(self):
        return f'#{self.word} для {self.chat}'

    class Meta:
        verbose_name = 'Стоп-слово'
        verbose_name_plural = 'Стоп-слова'


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'#{self.chat} - {self.date}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Лог'


class Dialog(models.Model):
    chat_id = models.CharField(max_length=200)
    name = models.TextField()
