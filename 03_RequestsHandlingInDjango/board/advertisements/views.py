from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView


class MainPage(View):
    def get(self, request):
        categories = ['Спорт', 'Развлечение', 'Учеба', 'Другое']
        regions = ['Москва', 'Питер', 'Подмосковье', 'Екатеринбург', 'Тверь', 'Пермь']
        return render(request, 'advertisements/advertisement_list.html', {'categories': categories, 'regions': regions})


ip_checker = {}

class ListAdvertisement(View):
    def get(self, request):
        ip = request.META.get("REMOTE_ADDR")
        ip_checker[ip] = {'get': ip_checker.get(ip, {'get': 0})['get'], 'post': ip_checker.get(ip, {'post': 0})['post']}
        if request.method == 'GET':
            ip_checker[ip]['get'] += 1
        else:
            ip_checker[ip]['post'] += 1
        now_count = ip_checker[ip]
        gdz = ['Python Basic', 'Python-фреймворк Django', 'frontend Разработчик', "Веб-верстка «Базовый уровень»", 'java - Разработчик']
        another = ['contacts', 'about-us', 'categories', 'regions']
        films = ['Довод', 'Душа', "Еще по одной", "Огонь"]
        songs = ['Like a Rolling Stone', '(I Can’t Get No) Satisfaction', 'Imagine', 'Good Vibrations']
        info_list = [gdz, another, films, songs]
        return render(request, 'advertisements/my_list_advertisement.html', {'info_list': info_list, 'now_count': now_count})

    def post(self, request):
        return HttpResponse('запрос на создание новой записи успешно выполнен')


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = 'Улица самая лучшая, дом 3'
        context['tel'] = '88007553535'
        context['email'] = 'megacompany@gmail.com'
        return context

class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_name'] = 'Булочная'
        context['company_about'] = 'Самый вкусный булочки'
        return context

