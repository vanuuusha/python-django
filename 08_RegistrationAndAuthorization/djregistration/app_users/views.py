from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views import View
from .forms import RegisterForm, LoginForm
from .models import UserProfile
from django.http import HttpResponse, HttpResponseRedirect


class RegisterView(View):
    def get(self, request):
        if not request.user.is_anonymous:
            return HttpResponse(
                                'Вы уже зарегистрированы'
                                '<a href="/">вернуть на главную страницу</a>'
            )
        form = RegisterForm()
        return render(request, 'app_users/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            telephone = form.cleaned_data.get('telephone')
            city = form.cleaned_data.get('city')
            UserProfile.objects.create(
                user=user,
                telephone=telephone,
                city=city,
            )
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
        return render(request, 'app_users/register.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class LoginView(View):
    def get(self, request):
        if not request.user.is_anonymous:
            return HttpResponse(
                                'Вы уже вошли в аккаунт'
                                '<a href="/">вернуть на главную страницу</a>'
                                )
        form = LoginForm()
        return render(request, 'app_users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
        return render(request, 'app_users/login.html', {'form': form})


class ProfileView(View):
    def get(self, request):
        return render(request, 'app_users/account.html', {})


