# Generated by Django 4.1.5 on 2024-03-30 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woow', '0005_ipmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='IpModel',
        ),
        migrations.RemoveField(
            model_name='post',
            name='address',
        ),
        migrations.AddField(
            model_name='post',
            name='book',
            field=models.FileField(default=2, upload_to='file/'),
            preserve_default=False,
        ),
    ]
