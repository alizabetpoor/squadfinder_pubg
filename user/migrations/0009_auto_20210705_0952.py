# Generated by Django 3.2.5 on 2021-07-05 05:22

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20210704_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_detail',
            name='role',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('sn', 'sniper'), ('ca', 'camper'), ('ru', 'rusher'), ('co', 'cover')], default=None, max_length=8),
        ),
        migrations.AlterField(
            model_name='account_detail',
            name='server',
            field=models.CharField(blank=True, choices=[('EU', 'europe'), ('AS', 'asia'), ('KO', 'korea'), ('AF', 'africa'), ('US', 'america')], default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='account_detail',
            name='start_season',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]