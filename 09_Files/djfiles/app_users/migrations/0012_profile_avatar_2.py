# Generated by Django 2.2 on 2021-08-31 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0011_auto_20210831_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar_2',
            field=models.FileField(default=None, null=True, upload_to='new_avatars/'),
        ),
    ]
