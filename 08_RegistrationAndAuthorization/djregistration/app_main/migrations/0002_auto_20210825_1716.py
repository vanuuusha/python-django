# Generated by Django 2.2 on 2021-08-25 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'permissions': (('can_publish', 'Может публиковать'),)},
        ),
        migrations.AlterModelTable(
            name='news',
            table='News',
        ),
    ]