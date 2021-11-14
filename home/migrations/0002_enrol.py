# Generated by Django 3.2.8 on 2021-11-10 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=128, verbose_name='학생')),
                ('room_id', models.CharField(default=None, max_length=128, verbose_name='방 아이디')),
                ('room_password', models.CharField(max_length=64, verbose_name='방 비밀번호')),
                ('room_name', models.CharField(max_length=128, verbose_name='방 이름')),
                ('make_date', models.DateTimeField(auto_now_add=True, verbose_name='등록 날짜')),
            ],
            options={
                'verbose_name': 'enrol 명단',
                'verbose_name_plural': 'enrol 명단',
                'db_table': 'enrol',
            },
        ),
    ]