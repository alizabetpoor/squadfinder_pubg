# Generated by Django 3.2.5 on 2021-07-04 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20210704_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_detail',
            name='player',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acc_detail', to=settings.AUTH_USER_MODEL),
        ),
    ]
