# Generated by Django 2.0.1 on 2018-04-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField()),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]
