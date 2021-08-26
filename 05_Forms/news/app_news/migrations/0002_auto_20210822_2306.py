# Generated by Django 2.2 on 2021-08-22 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=None, null=None, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=30, verbose_name='имя автора'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=300, verbose_name='содержимое комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(default=None, null=None, on_delete=django.db.models.deletion.CASCADE, related_name='Comment', to='app_news.News'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(max_length=3000, verbose_name='содержимое новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date_make',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата публикации новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(max_length=30, verbose_name='название новости'),
        ),
    ]