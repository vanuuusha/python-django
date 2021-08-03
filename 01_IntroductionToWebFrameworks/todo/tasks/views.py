from django.http import HttpResponse

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('<ul>'
                            '<li>Установить python(и Pycharm)</li>'
                            '<li>Установить django</li>'
                            '<li>Запустить сервер</li>'
                            '<li>Порадоваться результату</li>'
                            '<li>УРА УРА УРА!!</li>'
                            '</ul>')
