# Generated by Django 2.0.1 on 2018-04-12 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20180412_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
