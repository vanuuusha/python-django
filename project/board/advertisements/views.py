from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class AdvertisementsList(View):

    def get(self, request):
        gdz = {'python-basic': 'Python Basic', 'django': 'Python-фреймворк Django', 'frontend-developer': 'frontend Разработчик', 'layout-basic': "Веб-верстка «Базовый уровень»", 'java': 'java - Разработчик'}
        another = ['contacts', 'about-us', 'categories', 'regions']
        films = ['Довод', 'Душа', "Еще по одной", "Огонь"]
        songs = ['Like a Rolling Stone', '(I Can’t Get No) Satisfaction', 'Imagine', 'Good Vibrations']
        return render(request, "advertisements/advertisements_list.html", {"gdz": gdz, 'another': another, "films": films, "songs": songs})

    def post(self, request):
        return HttpResponse("Запись успешно добавлена")


def advertisement_deatails(request, *args, **kwargs):
    return HttpResponse("<ul>"
                        "<li>Описание что сделать 1</li>"
                        "<li>Описание что сделать 2</li>"
                        "<li>Описание что сделать 3</li>"
                        "<li>Описание что сделать 4</li>"
                        "<li>Описание что сделать 5</li>"
                        "</ul>")


def python_basic(request, *args, **kwargs):
    return render(request, 'advertisements/python_basic.html')


def django(request, *args, **kwargs):
    return render(request, 'advertisements/django.html')


def frontend_developer(request, *args, **kwargs):
    return render(request, 'advertisements/django.html')


def layout_basic(request, *args, **kwargs):
    return render(request, 'advertisements/layout_basic.html')


def java(request, *args, **kwargs):
    return render(request, 'advertisements/java.html')


def contacts(request, *args, **kwargs):
    telephone = 88007081945
    email = "sales@company.com"
    return render(request, 'advertisements/contacts.html', {'tel': telephone, "email": email})


def about_us(request,  *args, **kwargs):
    name = "Вкусные булочки"
    about = "Продaем лучшие булочки"
    return render(request, 'advertisements/about-us.html', {'name': name, 'about': about})


def categories_page(request,  *args, **kwargs):
    categories = ['личные вещи', 'транспорт', 'хобби', 'отдых']
    return render(request, 'advertisements/categories.html', {'categories': categories})


class RegionsPage(View):

    def get(self, request):
        regions = ['Москва', 'Московская область', 'республика Алтай', 'Вологодская область']
        return render(request, 'advertisements/regions.html', {'regions': regions})

    def post(self, request):
        return HttpResponse('Регион успешно создан')

