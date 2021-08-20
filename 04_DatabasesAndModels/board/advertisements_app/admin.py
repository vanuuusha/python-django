from django.contrib import admin

from .models import Advertisement, AdvertisementAuthor, AdvertisementChapter, Restaurant, Waiter


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title', 'description')
    ordering = ('id', 'title')
    search_fields = ('description', )


class AdvertisementAuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )


class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Личная информация', {
            'fields': ('name', 'description', 'phone', 'country', 'city', 'street', 'house'),
            'description': 'Личное'
                               }),
        ('Сервисы', {
            'fields': ('serves_hot_dogs', 'serves_pizza', 'serves_sushi', 'serves_burgers', 'serves_donats', 'serves_coffee')
        }),
        ('Информация по месту работы', {
            'fields': ('count_of_employers', 'director', 'chef')
        })
    )


class WaiterAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Про человека', {
            'fields': ('first_name', 'last_name', 'age', 'sex', 'restaurant')
        }),
        ('Место жительства', {
            'fields': ('country', 'city', 'street', 'house', 'apartment')
        }),
        ('Образование', {
            'fields': ('seniority', 'education', 'cources')
        })
    )


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Waiter, WaiterAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(AdvertisementAuthor, AdvertisementAuthorAdmin)
admin.site.register(AdvertisementChapter)

