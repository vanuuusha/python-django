from django.shortcuts import render
from .models import Blog, FileForBlog
from django.views import View
from .forms import AddBlogForm
from django.http import HttpResponseRedirect
from django.conf import settings

class ListBlogView(View):
    def get(self, request):
        context = {'blogs': Blog.objects.order_by('-date_create')}
        return render(request, 'app_blog/blog_list.html', context=context)


class AddBlogView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = AddBlogForm()
            context = {'form': form, 'author': request.user.username}
            return render(request, 'app_blog/add_blog.html', context)
        return HttpResponseRedirect('/')
    
    def post(self, request):
        form = AddBlogForm(request.POST, request.FILES)
        for file in request.FILES.getlist('file_field'):
            if not (file.name.endswith('.jpg') or file.name.endswith('.png')):
                form.add_error('__all__',  'Файлы должны иметь расширение jpg или png')
                break
        else:
            if form.is_valid():
                form = form.cleaned_data
                blog = Blog.objects.create(
                    author=request.user.username,
                    title=form['title'],
                    content=form['content'],
                )
                for file in request.FILES.getlist('file_field'):
                    FileForBlog.objects.create(
                        blog=blog,
                        file_field=file,
                    )
                return HttpResponseRedirect('/')
        context = {'form': form, 'author': request.user.username}
        return render(request, 'app_blog/add_blog.html', context)


class DetailBlogView(View):
    def get(self, request, **kwargs):
        blog_id = kwargs.get('pk')
        blog = Blog.objects.get(id=blog_id)
        context = {'blog': blog, 'url': settings.MEDIA_URL}
        return render(request, 'app_blog/detail_blog.html', context=context)
