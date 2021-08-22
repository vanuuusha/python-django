from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from .models import News, Comment
from .forms import AddNewsForm, AddCommentFormAuth, AddCommentFormAnon
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


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
        context['comment_form'] = AddCommentFormAnon()
        context['comments'] = self.object.Comment.all()
        return context

    def post(self, request, **kwargs):
        if request.user.is_authenticated:
            form = AddCommentFormAuth(request.POST)
        else:
            form = AddCommentFormAnon(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            form['news'] = News.objects.filter(id=kwargs.get('pk'))[0]
            if request.user.is_authenticated:
                form['author'] = request.user.username
                form['user'] = User.objects.filter(id=request.user.id)[0]
            else:
                form['author'] = ' '.join([form['author'], '(Аноним)'])
                form['user'] = User.objects.filter(id=4)[0]
            Comment.objects.create(**form)
            return HttpResponseRedirect('/list-news/')
        
        # вот тут не очень понял, как сделать чтоб форма отображалась с ошибками, а не создавалась новая и еще,
        # если раскоментить то, что у меня в файлике forms почему-то не один комент валидацию не проходит
        #  Указывайте свои TODO чтобы вопросы было легче искать. Честно говоря не понял проблему, где не
        #  отображаются ошибки? Если не вводя комментарий в детальном представлении новости нажать "Добавить
        #  комментарий" то выводится подсказка где должно быть заполнено.
        
        #  ну это да, но это проверяет вроде html еще, а вот я теперь поставь критерий на автора, и
        #  если отправить форму где автор aaaa, то он просто перезапустит страницу без ошибок и ранее введенных
        #  данных, что вроде бы логично, ведь я вызываю метод get без аргумента этой формы, но не знаю как передать его
        return render(request, self.template_name, {'comment_form': form})  # TODO если валидация не пройдена возвращаем
                                                                            #  форму с ошибкой обратно


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


class Main(View):
    def get(self, request):
        return render(request, 'app_news/main.html', {})
        