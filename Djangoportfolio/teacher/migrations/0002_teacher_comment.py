# Generated by Django 5.1 on 2024-09-10 11:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='comment',
            field=models.TextField(default=datetime.datetime(2024, 9, 10, 11, 19, 48, 785891, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
