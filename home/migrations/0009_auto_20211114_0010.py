# Generated by Django 2.2.14 on 2021-11-13 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20211114_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='maker',
            field=models.CharField(default='NULL', max_length=64, verbose_name='생성자'),
        ),
    ]