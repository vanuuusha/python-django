# Generated by Django 2.2 on 2021-08-25 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0002_auto_20210825_1431'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('can_vaerivicate', 'может верифицировать'),)},
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table='Profile',
        ),
    ]