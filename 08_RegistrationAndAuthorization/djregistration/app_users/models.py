from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=15)
    flag = models.BooleanField(default=False, verbose_name='Верификация')
    count_published_news = models.IntegerField(default=0)

    class Meta:
        db_table = 'Profile'
        permissions = (
            ('can_vaerivicate', 'может верифицировать'),
        )

    def __str__(self):
        return self.user.username

