from django.shortcuts import render
from .forms import AuthForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import datetime
from django.contrib.auth.views import LoginView


class Auth(View):
    def get(self, request):
        form = AuthForm()
        context = {
            'form': form
        }
        return render(request, 'app_users/auth.html', context=context)

    def post(self, request):
        form = AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            hour = datetime.datetime.now().hour
            if not (hour > 23 or hour < 8):
                if user:
                    if user.is_active:
                        if not user.is_superuser or username == "Vanusha":
                            login(request, user)
                            return HttpResponse('Вы успешно вошли в систему')
                        else:
                            form.add_error('__all__', 'Вы админ=(')
                    else:
                        form.add_error('__all__', 'Ошибка! учетная запись пользователя недоступна')
                else:
                    form.add_error('__all__', 'Неверно введен логин или пароль')
            else: 
                form.add_error('__all__', 'Сейчас регистрация запрещена')
        context = {
            'form': form
        }
        return render(request, 'app_users/auth.html', context=context)


# class AnotherAuth(LoginView):
#    template_name = 'app_users/auth.html'


def logout_view(request):
    logout(request)
    return HttpResponse('Вы успешно вышли из аккаунта')