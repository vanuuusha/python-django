from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from .forms import AuthForm, CreateUserForm, AccountRadactForm
from django.http import HttpResponseRedirect
from .models import Profile
from django.conf import settings


class UserLogin(View):
    def get(self, request):
        form = AuthForm()
        context = {'form': form}
        return render(request, 'app_users/login.html', context=context)

    def post(self, request):
        form = AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    form.add_error('__all__', 'Ваш аккаунт не активирован')
            else:
                form.add_error('__all__', 'Неверный логин или пароль')
        context = {'form': form}
        return render(request, 'app_users/login.html', context=context)


class UserRegister(View):
    def get(self, request):
        form = CreateUserForm()
        context = {'form': form}
        return render(request, 'app_users/register.html', context=context)

    def post(self, request):
        form = CreateUserForm(request.POST)
        if not request.user.is_anonymous:
            form.add_error('__all__', 'Вы уже зарегистрированы')
        if form.is_valid() and request.user.is_anonymous:
            user = form.save()
            form = form.cleaned_data
            telephone = form['telephone']
            Profile.objects.create(
                user=user,
                telephone=telephone)
            authenticate(password=form['password1'], username=form['username'])
            login(request, user)
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'app_users/register.html', context=context)


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return HttpResponseRedirect('/')


class AccountView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = AccountRadactForm(instance=request.user, initial={
                'telephone': request.user.profile.telephone,
            })
            context = {'form': form, 'url': settings.MEDIA_URL}
            return render(request, 'app_users/account.html', context=context)
        return HttpResponseRedirect('/')

    def post(self, request):
        form = AccountRadactForm(request.POST, request.FILES, instance=request.user, initial={
            'telephone': request.user.profile.telephone,
            })
        if request.FILES.getlist('avatar'):
            file = request.FILES.getlist('avatar')[0]
            if request.user.profile.avatar:
                request.user.profile.avatar.delete()
                request.user.profile.save()
            request.user.profile.avatar = file
            request.user.profile.save()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/users/account/')

        context = {'form': form}
        return render(request, 'app_users/account.html', context=context)
