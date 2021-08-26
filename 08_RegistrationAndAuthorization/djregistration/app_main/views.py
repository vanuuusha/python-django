from django.shortcuts import render
from django.views import View
from .models import News, Comment
from .forms import CommentForm, NewsForm, ModerForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import Group


class MainView(View):
    def get(self, request):
        return render(request, 'app_main/main.html', {})


class ListNewsView(View):
    def get(self, request):
        if request.user.userprofile.flag:
            my_group = Group.objects.get(name='Верицифицированный пользователь')
            my_group.user_set.add(request.user)
        template_name = 'app_main/list_news.html'
        news = News.objects.filter(published=True)[:25]
        perm = True if request.user.has_perm('app_main.add_news') else False
        moder = True if request.user.has_perm('app_main.can_publish_news') else False
        return render(request, template_name, {'news': news, 'perm': perm, 'moder': moder})


class DetailNewsView(View):
    def get(self, request, **kwargs):
        new = News.objects.get(id=self.kwargs['pk'])
        form = CommentForm()
        comments = Comment.objects.filter(news=new)
        can_add = request.user.has_perm('app_main.add_news')
        return render(request, 'app_main/detail.html', {'new': new, 'form': form,
                                                        'comments': comments, 'can_add': can_add})

    def post(self, request, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            form['author'] = request.user.username
            form['news'] = News.objects.get(id=self.kwargs['pk'])
            form['user'] = request.user
            Comment.objects.create(**form)
            return HttpResponseRedirect(''.join(['/list-news/', str(kwargs['pk'])]))
        new = News.objects.get(id=self.kwargs['pk'])
        comments = Comment.objects.filter(news=new)
        can_add = request.user.has_perm('app_main.add_news')
        return render(request, 'app_main/detail.html', {'new': new, 'form': form,
                                                        'comments': comments, 'can_add': can_add})


class CreateNewsView(View):
    def get(self, request):
        if request.user.has_perm('app_main.add_comment'):
            form = NewsForm()
            return render(request, 'app_main/create_news.html', {'form': form})
        return HttpResponse(
            '<p>Вы не верифицированный пользователь</p>'
            '<a href="/">Вернуться на главную</a>'
        )

    def post(self, request):
        form = NewsForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            form['author'] = request.user.username
            News.objects.create(**form)
            request.user.userprofile.count_published_news += 1
            request.user.userprofile.save()
            return HttpResponse(
                '<p>Ваша новость успешно добавлена, вы сможете ее увидеть, когда модератор проверит ее</p>'
                '<a href="/">Вернуться на главную</a>'
            )


class ModeratorView(View):
    def get(self, request):
        if request.user.has_perm('app_main.add_news'):
            perm = moder = True
            news = News.objects.filter(published=False)
            form = ModerForm()
            return render(request, 'app_main/moder_page.html', {'perm': perm, 'moder': moder,
                                                                'news': news, 'form': form})

        return HttpResponse(
                '<p>Вы не модератор, как вы нашли эту ссылку???</p>'
                '<a href="/">Вернуться на главную</a>'
            )

    def post(self, request):
        pass
    # а как тут выбирать, какую именно новость опубликовать/удалить?
    # TODO В шаблоне надо вывести все каждую новость со своим элементом <select> c одним выбором, а в этом методе надо
    #  получить данные о выборе пользователя и выполнить необходимые действия над каждой новостью. Чтобы
    #  идентифицировать select и новость, можно использовать какой-либо параметр <select>, например значение id сделать
    #  таким же как у id записи новости


