# Generated by Django 4.2.7 on 2023-11-26 07:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Potency',
            new_name='RemedyPotency',
        ),
        migrations.AlterField(
            model_name='remedy',
            name='lastUpdated',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 26, 1, 11, 56, 754575)),
        ),
    ]
