from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=20, blank=True)
    card = models.CharField(max_length=16, blank=True)
    telephone = models.CharField(max_length=10, blank=True)

    class Meta:
        db_table = 'Profile'

