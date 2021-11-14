# Generated by Django 3.2.8 on 2021-11-14 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20211113_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(default='NULL', max_length=128, verbose_name='방 ID')),
                ('writer', models.EmailField(default='NULL', max_length=128, verbose_name='작성자 email')),
                ('writername', models.CharField(default='NULL', max_length=128, verbose_name='작성자 이름')),
                ('title', models.CharField(default='NULL', max_length=128, verbose_name='제목')),
                ('description', models.CharField(default='NULL', max_length=1000, verbose_name='내용')),
                ('make_date', models.DateTimeField(auto_now_add=True, verbose_name='작성 날짜')),
            ],
        ),
        migrations.AlterField(
            model_name='analytics',
            name='room_id',
            field=models.CharField(default='NULL', max_length=128, verbose_name='방 ID'),
        ),
        migrations.AlterField(
            model_name='enrol',
            name='room_id',
            field=models.CharField(default=None, max_length=128, verbose_name='방 ID'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(default=None, max_length=128, verbose_name='방 ID'),
        ),
    ]
