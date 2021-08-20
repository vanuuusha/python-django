# Generated by Django 2.2 on 2021-08-17 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Flags',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('content', models.TextField(max_length=3000)),
                ('date_make', models.DateTimeField(auto_now_add=True)),
                ('date_corrected', models.DateTimeField(auto_now=True)),
                ('flag', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='News', to='app_news.NewsFlag')),
            ],
            options={
                'db_table': 'News',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('content', models.TextField(max_length=300)),
                ('news', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Comment', to='app_news.News')),
            ],
            options={
                'db_table': 'Comment',
                'ordering': ['id'],
            },
        ),
    ]