# Generated by Django 3.2.5 on 2021-07-30 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20210730_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squad_article',
            name='min_level',
            field=models.IntegerField(verbose_name='حداقل level'),
        ),
        migrations.AlterField(
            model_name='squad_article',
            name='min_time_to_play',
            field=models.IntegerField(verbose_name='حداقل تایم بازی در روز'),
        ),
    ]
