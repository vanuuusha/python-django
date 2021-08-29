from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from .models import Goods, HistoryUpload
from .forms import LoadPriceForm
import datetime
from django.conf import settings
import os


class GoodsList(ListView):
    template_name = 'app_goods/list-goods.html'
    context_object_name = 'goods'
    queryset = Goods.objects.all()


class GoodsLoad(View):
    def get(self, request):
        context = {'form': LoadPriceForm()}
        return render(request, 'app_goods/load.html', context=context)

    def post(self, request):
        form = LoadPriceForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            if file.name.endswith('.txt'):
                file.name = ''.join([datetime.datetime.now().strftime("%Y-%m-%d-%H.%M.%S"), file.name])
                filename = file.name
                HistoryUpload.objects.create(file=file)
                url = settings.BASE_DIR
                with open(os.path.join(url, 'media', 'file', filename)) as file:
                    text = file.read().split('\n')
                count_update = 0
                bad_articles = []
                for line in text:
                    line = line.split(':')
                    if Goods.objects.filter(code=line[0]):
                        if Goods.objects.filter(code=line[0])[0].price != int(line[1]):
                            Goods.objects.filter(code=line[0]).update(price=int(line[1]))
                            count_update += 1
                    else:
                        bad_articles.append(line[0])
                count_objects = Goods.objects.count()
                return HttpResponse(f"<p>Исправлено цен: {count_update}</p>"
                                    f"<p>Осталось не тронутыми цен: {count_objects - count_update}</p>"
                                    f"<p>Неправильные артикулы: {', '.join(bad_articles) if bad_articles else 'Пусто'}</p>")
            form.errors.add('__all__', 'Неправильное расширение файла (нужно txt)')
        context = {'form': form}
        return render(request, 'app_goods/load.html', context=context)
