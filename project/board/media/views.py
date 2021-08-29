from django.shortcuts import render
from django.views import View
from .forms import FileForm, FileCheckerForm
from django.http import HttpResponse
from .my_scripts.file_checker import correct


class FileView(View):
    def get(self, request):
        form = FileForm()
        context = {'form': form}
        return render(request, 'media/file.html', context=context)

    def post(self, request):
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            return HttpResponse(content=''.join(['Название файла: ', file.name, '<br>Размер файла: ', str(file.size), 'б']), status=200)
        context = {'form': form}
        return render(request, 'media/file.html', context=context)


class FileCheckView(View):
    def get(self, request):
        form = FileCheckerForm()
        context = {'form': form}
        return render(request, 'media/file.html', context=context)

    def post(self, request):
        form = FileCheckerForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            if correct(file.read().decode('utf-8')) and file.name.endswith('.txt'):
                return HttpResponse("Все хорошо!")
            return HttpResponse("Файл не прошел проверку")
        context = {'form': form}
        return render(request, 'media/file.html', context=context)