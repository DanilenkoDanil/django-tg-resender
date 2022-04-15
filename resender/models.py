from django.db import models


class MyChat(models.Model):
    name = models.CharField(max_length=200)
    chat_id = models.CharField(max_length=200)

    def __str__(self):
        return f'#{self.name}'

    class Meta:
        verbose_name = 'Мой чат'
        verbose_name_plural = 'Мои чаты'


class Chat(models.Model):
    name = models.CharField(max_length=200)
    chat_id = models.CharField(max_length=200)

    def __str__(self):
        return f'#{self.name}'

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class WhiteWord(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    my_chat = models.ForeignKey(MyChat, on_delete=models.CASCADE, blank=True, null=True)
    word = models.CharField(max_length=200)

    def __str__(self):
        return f'#{self.word} для {self.chat}'

    class Meta:
        verbose_name = 'Белое слово'
        verbose_name_plural = 'Белые слова'


class BlackWord(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)

    def __str__(self):
        return f'#{self.word} для {self.chat}'

    class Meta:
        verbose_name = 'Черное слово'
        verbose_name_plural = 'Черные слова'


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'#{self.chat} - {self.date}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Dialog(models.Model):
    chat_id = models.CharField(max_length=200)
    name = models.TextField()
