from django.contrib import admin

from .models import Advertisement, AdvertisementAuthor, AdvertisementChapter


@admin.register(Advertisement, AdvertisementAuthor, AdvertisementChapter)
class AdvertisementAdmin(admin.ModelAdmin):
    pass
