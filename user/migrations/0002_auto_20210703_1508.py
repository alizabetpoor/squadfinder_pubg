# Generated by Django 3.1.3 on 2021-07-03 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phonenumber',
            field=models.CharField(blank=True, default=None, max_length=13, null=True, unique=True, verbose_name='شماره موبایل'),
        ),
    ]