# Generated by Django 4.2.7 on 2023-11-30 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeo', '0003_remove_materiamedica_remedy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remedy',
            name='materiaMedica',
            field=models.ManyToManyField(to='homeo.materiamedica'),
        ),
        migrations.AlterField(
            model_name='remedy',
            name='potency',
            field=models.ManyToManyField(to='homeo.potencylist'),
        ),
    ]