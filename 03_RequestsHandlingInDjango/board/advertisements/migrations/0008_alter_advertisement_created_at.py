# Generated by Django 3.2.6 on 2021-08-13 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0007_alter_advertisement_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
