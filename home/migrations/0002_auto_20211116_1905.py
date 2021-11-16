# Generated by Django 3.2.8 on 2021-11-16 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analytics',
            name='count',
        ),
        migrations.RemoveField(
            model_name='analytics',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='analytics',
            name='time',
        ),
        migrations.AddField(
            model_name='analytics',
            name='quiz',
            field=models.IntegerField(default=0, verbose_name='퀴즈 점수'),
        ),
    ]