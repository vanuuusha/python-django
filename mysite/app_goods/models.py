from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    price = models.IntegerField()


class HistoryUpload(models.Model):
    file = models.FileField(upload_to='file/')
