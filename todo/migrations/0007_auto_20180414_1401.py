# Generated by Django 2.0.1 on 2018-04-14 13:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20180412_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='mydate',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 4, 14, 13, 1, 45, 424678, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]