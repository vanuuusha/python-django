from django.db import models


class News(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField(max_length=3000)
    date_make = models.DateTimeField(auto_now_add=True)
    date_corrected = models.DateTimeField(auto_now=True)
    flag = models.ForeignKey('NewsFlag', related_name='News', null=True, default=None,
                             on_delete=models.CASCADE)

    class Meta:
        db_table = 'News'
        ordering = ['id']


class Comment(models.Model):
    author = models.CharField(max_length=30)
    content = models.TextField(max_length=300)
    news = models.ForeignKey('News', related_name='Comment', null=True, default=None,
                             on_delete=models.CASCADE)

    class Meta:
        db_table = 'Comment'
        ordering = ['id']


class NewsFlag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Flags'
        ordering = ['id']
