# Generated by Django 2.2.14 on 2021-11-11 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_quiz_room_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]