from django.contrib import admin
from .models import Vacancy, Resume


class VacancyAdmin(admin.ModelAdmin):
    pass


class ResumeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Resume, ResumeAdmin)


