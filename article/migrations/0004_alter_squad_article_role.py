# Generated by Django 3.2.5 on 2021-07-26 09:42

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20210706_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squad_article',
            name='role',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('sn', 'sniper'), ('ca', 'camper'), ('ru', 'rusher'), ('co', 'cover')], max_length=11, verbose_name='نقش'),
        ),
    ]
