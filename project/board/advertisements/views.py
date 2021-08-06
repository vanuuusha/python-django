from django.shortcuts import render
from django.http import HttpResponse

def advertisements_list(request, *args, **kwargs):
    return render(request, "advertisements/advertisements_list.html")


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