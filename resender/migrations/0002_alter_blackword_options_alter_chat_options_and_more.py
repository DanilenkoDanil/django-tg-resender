# Generated by Django 4.0.4 on 2022-04-13 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resender', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blackword',
            options={'verbose_name': 'Черное слово', 'verbose_name_plural': 'Черные слова'},
        ),
        migrations.AlterModelOptions(
            name='chat',
            options={'verbose_name': 'Чат', 'verbose_name_plural': 'Чаты'},
        ),
        migrations.AlterModelOptions(
            name='mychat',
            options={'verbose_name': 'Мой чат', 'verbose_name_plural': 'Мои чаты'},
        ),
        migrations.AlterModelOptions(
            name='whiteword',
            options={'verbose_name': 'Белое слово', 'verbose_name_plural': 'Белые слова'},
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resender.chat')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]
