# Generated by Django 2.2.5 on 2019-10-08 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191008_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 8, 17, 44, 16, 952883)),
        ),
    ]
