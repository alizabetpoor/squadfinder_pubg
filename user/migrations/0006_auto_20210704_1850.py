# Generated by Django 3.2.5 on 2021-07-04 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210704_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='acc_detail',
        ),
        migrations.AddField(
            model_name='account_detail',
            name='player',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='acc_detail', to=settings.AUTH_USER_MODEL),
        ),
    ]
