# Generated by Django 3.2.8 on 2021-11-11 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_room_room_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='질문 아이디')),
                ('question', models.CharField(max_length=64, verbose_name='질문')),
                ('item1', models.CharField(max_length=128, verbose_name='질문지1')),
                ('item2', models.CharField(max_length=128, verbose_name='질문지2')),
                ('item3', models.CharField(max_length=128, verbose_name='질문지3')),
                ('item4', models.CharField(max_length=128, verbose_name='질문지4')),
                ('answer', models.IntegerField(default=None, verbose_name='정답')),
                ('room_id', models.ForeignKey(db_column='room_id', on_delete=django.db.models.deletion.CASCADE, to='home.room')),
            ],
            options={
                'verbose_name': 'Quiz 명단',
                'verbose_name_plural': 'Quiz 명단',
                'db_table': 'Quiz',
            },
        ),
    ]
