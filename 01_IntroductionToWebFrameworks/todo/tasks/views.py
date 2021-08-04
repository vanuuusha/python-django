from django.http import HttpResponse

from django.views import View

from random import choice

TASKS = ['проснуться', 'позавтракать', 'пойти что-то делать', 'каточка в кс', 'пойти спать', 'скачать Pycharm', 'Установить django', 'Запустить сервер', 'Порадоваться результату']

class ToDoView(View):

    def get(self, request, *args, **kwargs):
        tasks = TASKS[:] # для того, чтобы не повторялись задачи
        server_answer = '<ul>'
        for _ in range(5):
            now_task = choice(tasks)
            tasks.remove(now_task)
            server_answer = ''.join([server_answer, '<li>', now_task, '</li>'])
        server_answer = ''.join([server_answer, '</ul>'])

        return HttpResponse(server_answer)
