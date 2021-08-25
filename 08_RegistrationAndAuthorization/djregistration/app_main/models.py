from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    published = models.BooleanField(default=False)

    class Meta:
        db_table = 'News'
        permissions = (
            ('can_publish', 'Может публиковать'),
        )

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    news = models.ForeignKey(News, related_name='Comment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='User', on_delete=True, default=None, null=None)
