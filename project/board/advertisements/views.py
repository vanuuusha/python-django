from django.shortcuts import render
from django.http import HttpResponse
import os

def get_url(filename):
    cwd = os.path.join(os.getcwd(), 'advertisements', 'templates', 'advertisements', filename)
    with open(cwd, mode='r', encoding='utf') as file:
        text = file.read()
    return text

def advertisements_list(request, *args, **kwargs):
    return HttpResponse("<h1>Прошел все курсы на Skillbox. Продаю готовые решения!!!</h1>"
                        "<ul>"
                        "<li><a href='/python-basic'>Python Basic</a></li>"
                        "<li><a href='/django'>Python-фреймворк Django</a></li>"
                        "<li><a href='/frontend-developer'>frontend Разработчик</a></li>"
                        "<li><a href='/layout-basic'>Веб-верстка «Базовый уровень»</a></li>"
                        "<li><a href='/java'>java - Разработчик</a></li>"
                        "</ul>")


def advertisement_deatails(request, *args, **kwargs):
    return HttpResponse("<ul>"
                        "<li>Описание что сделать 1</li>"
                        "<li>Описание что сделать 2</li>"
                        "<li>Описание что сделать 3</li>"
                        "<li>Описание что сделать 4</li>"
                        "<li>Описание что сделать 5</li>"
                        "</ul>")


def python_basic(request, *args, **kwargs):
    text = get_url("python_basic.html")
    return HttpResponse(text)


def django(request, *args, **kwargs):
    text = get_url("django.html")
    return HttpResponse(text)


def frontend_developer(request, *args, **kwargs):
    text = get_url("frontend_developer.html")
    return HttpResponse(text)


def layout_basic(request, *args, **kwargs):
    text = get_url("layout_basic.html")
    return HttpResponse(text)


def java(request, *args, **kwargs):
    text = get_url("java.html")
    return HttpResponse(text)
