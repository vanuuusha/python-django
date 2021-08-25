from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views import View
from .models import Vacancy


class ListVacancyView(View):
    def get(self, request):
        if not request.user.has_perm('app_permissions.view_vacancy'): #<app>.<action>_<object_name>
            raise PermissionDenied()
        vacancy = Vacancy.objects.all()[:10]
        return render(request, 'app_permissions/list_vacancy.html', {'vacancy': vacancy})
    
        


