from django.shortcuts import render
from .forms import AuthForm, MyUserCreationForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from .models import Profile
# from django.contrib.auth.views import LoginView
# from django.contrib.auth.models import User


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
    return HttpResponseRedirect('/')


class AccountView(View):

    def get(self, request):
        return render(request, 'app_users/account.html')


class RegistrationView(View):

    def get(self, request):
        form = MyUserCreationForm()
        return render(request, 'app_users/register.html', {'form': form})

    def post(self, request):
        form = MyUserCreationForm(request.POST)
        if not request.user.is_anonymous:
            form.add_error('__all__', 'Вы уже зарегистрированы')
        if form.is_valid() and request.user.is_anonymous:
            user = form.save()
            date_of_birth = form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            card = form.cleaned_data.get('card')
            telephone = form.cleaned_data.get('telephone')

            Profile.objects.create(
                user=user,
                date_of_birth=date_of_birth,
                city=city,
                card=card,
                telephone=telephone,
            )

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
        return render(request, 'app_users/register.html', {'form': form})
            