from django.db import models


class Resume(models.Model):
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    description = models.TextField(default='', verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published_at = models.DateTimeField(verbose_name='Дата публикации', blank=True, null=True)


class Vacancy(models.Model):
    is_active = models.BooleanField(default=False, verbose_name='Активно')
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    description = models.TextField(default='', verbose_name='Описание')
    published = models.CharField(max_length=30, verbose_name='Кто опубликовал')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published_at = models.DateTimeField(verbose_name='Дата публикации', blank=True, null=True)

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'
        permissions = [
            ("Can_publish", 'Может опубликовать')
        ]
        db_table = 'Vacancy'

    def __str__(self):
        return self.title
