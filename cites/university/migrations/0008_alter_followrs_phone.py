# Generated by Django 4.0.6 on 2022-12-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0007_followrs_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followrs',
            name='phone',
            field=models.IntegerField(null=True, unique=True, verbose_name='phone'),
        ),
    ]
