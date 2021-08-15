from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1500, verbose_name='название объявление', db_index=True)
    description = models.TextField(verbose_name='описание объявления')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.IntegerField(verbose_name='цена', default=0)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements')
    typpe = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE,
                              related_name='advertisements')

    class Meta:
        db_table = 'advertisements'
        ordering = ['id']


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100)
