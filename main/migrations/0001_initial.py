# Generated by Django 3.2.8 on 2021-11-16 13:17

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=128, verbose_name='이메일')),
                ('username', models.CharField(max_length=64, verbose_name='이름')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('registerd_date', models.DateTimeField(auto_now_add=True, verbose_name='가입시간')),
                ('image', models.ImageField(default='face-recognition.png', storage=main.models.OverwriteStorage(), upload_to='profile', verbose_name='이미지')),
                ('role', models.CharField(max_length=10, verbose_name='신분')),
                ('check', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '사용자 명단',
                'verbose_name_plural': '사용자 명단',
                'db_table': 'user',
            },
        ),
    ]
