from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

from .forms import LoginForm, CustomUserRegisterForm


def login_view(request):
    """ функция авторизации пользователя """

    form = LoginForm()
    template_name = "login.html"
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            template_name = "profile.html"
        else:
            template_name = "register_false.html"
    context = {'form': form}
    return render(request, template_name, context)


def register_view(request):
    """ функция регистрации пользователя на сайте """

    form = CustomUserRegisterForm()
    if request.method == 'POST':
        try:
            new_user = CustomUserRegisterForm(request.POST)
            new_user.save()
            return render(request, 'successful_register.html')
        except BaseException:
            return render(request, "register_false.html")

    context = {'form': form}
    return render(request, 'register_form.html', context)


def get_profile(request):
    """ функция для отображения профиля авторизованного пользователя """
    return render(request, 'profile.html')


def logout_view(request):
    """ функция выхода из аккаунта пользователя """
    logout(request)
    return render(request, 'start_page.html')
