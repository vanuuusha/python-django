from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название объявления')
    description = models.TextField(verbose_name='Описание объявления')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.IntegerField(verbose_name='цена', default=0)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    author = models.ForeignKey('AdvertisementAuthor', related_name='advertisement', on_delete=models.CASCADE,
                               null=True, default=None)
    chapter = models.ForeignKey('AdvertisementChapter', related_name='advertisement',
                                on_delete=models.CASCADE, null=True, default=None)

    class Meta:
        db_table = 'advertisement'
        ordering = ['id']


class AdvertisementAuthor(models.Model):
    name = models.CharField(max_length=30)
    mail = models.CharField(max_length=200)
    telephone = models.CharField(max_length=50)

    class Meta:
        db_table = 'advertisement_author'
        
    def __str__(self):
        return ' '.join(['name:', self.name, 'email:', self.mail, 'phone:', self.telephone])


class AdvertisementChapter(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'advertisement_chapter'
