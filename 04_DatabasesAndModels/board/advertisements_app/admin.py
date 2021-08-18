from django.contrib import admin

from .models import Advertisement, AdvertisementAuthor, AdvertisementChapter


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title', 'description')
    ordering = ('id', 'title')
    search_fields = ('description', )


class AdvertisementAuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )


admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(AdvertisementAuthor, AdvertisementAuthorAdmin)
admin.site.register(AdvertisementChapter)

