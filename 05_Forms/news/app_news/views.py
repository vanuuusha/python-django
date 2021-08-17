from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from .models import News, Comment
from .forms import AddNewsForm, AddCommentForm
from django.http import HttpResponseRedirect


class ListNews(ListView):
    model = News
    template_name = 'app_news/list_news.html'
    context_object_name = 'news'
    queryset = News.objects.all()


class DetailNews(DetailView):
    model = News
    template_name = 'app_news/detail.html'
    context_object_name = 'new'

    def get_context_data(self, form=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = AddCommentForm()
        context['comments'] = self.object.Comment.all()
        return context

    def post(self, request, **kwargs):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            # тут kwargs так как self.object не работает
            form['news'] = News.objects.filter(id=kwargs.get('pk'))[0]
            Comment.objects.create(**form)
            return HttpResponseRedirect('/list-news/')
        # вот тут не очень понял, как сделать чтоб форма отображалась с ошибками, а не создавалась новая и еще, если раскоментить то, что у меня в файлике forms почему-то не один комент валидацию не проходит
        return super().get(request=request, **kwargs)


class AddNews(View):

    def get(self, request):
        form = AddNewsForm()
        return render(request, 'app_news/add_new.html', context={'form': form})

    def post(self, request):
        form = AddNewsForm(request.POST)
        if form.is_valid():
            News.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/list-news/')
        return render(request, 'app_news/add_new.html', context={'form': form})
