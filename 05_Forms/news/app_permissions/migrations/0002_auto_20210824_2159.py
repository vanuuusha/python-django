# Generated by Django 2.2 on 2021-08-24 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_permissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'permissions': [('Can_publish', 'Может опубликовать')], 'verbose_name': 'вакансия', 'verbose_name_plural': 'вакансии'},
        ),
    ]
