# Generated by Django 3.2.5 on 2021-07-30 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20210730_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='ایمیل')),
                ('join', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
