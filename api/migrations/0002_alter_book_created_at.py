# Generated by Django 3.2.3 on 2021-05-14 05:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 5, 14, 5, 7, 7, 360578, tzinfo=utc)),
        ),
    ]
