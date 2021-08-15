# Generated by Django 3.2.6 on 2021-08-12 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0003_auto_20210812_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='advertisement',
            name='typpe',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisements.advertisementtype'),
        ),
    ]
