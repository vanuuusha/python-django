from django.contrib import admin
from .models import UserProfile


class UserProfileAmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAmin)
