import secrets
import string

from django.db import IntegrityError
from django.shortcuts import render, redirect
from accounts.models import CustomUser

from .models import ShortLink
from .forms import ShortLinkForm


def start_page(request):
    """ стартовая страница сайта """
    return render(request, 'start_page.html')


def generate_short_url(length):
    """ метод трансформации длинной ссылки в короткую """

    first_part_url = 'http://127.0.0.1:8000/'
    letters_digits = string.ascii_letters + string.digits
    last_part_url = ''.join(secrets.choice(letters_digits) for i in range(length))
    return first_part_url + last_part_url


def short_link(request):
    """ функция для получения пользователем короткой ссылки из длинной """

    form = ShortLinkForm()
    if request.user.username:
        user = CustomUser.objects.get(username=request.user.username)
        if request.method == 'POST':
            link = ShortLink(full_link=request.POST.get("full_link"), user=user, slug=generate_short_url(6))
            try:
                link.save()
            except IntegrityError:
                link = ShortLink.objects.get(full_link=request.POST.get("full_link"))
            context = {'link': link}
            return render(request, "transformation.html", context)
    context = {'form': form}
    return render(request, 'short_link.html', context)


def revers_transformation(request, slug):
    """ функция перенаправления на страницу с полным url-адресом """

    link = ShortLink.objects.get(slug='http://127.0.0.1:8000/' + slug)
    return redirect(link.full_link)


def list_links(request):
    """ функция вывода списка сокращенных ссылок авторизованного пользователя """

    if request.user.username:
        user = CustomUser.objects.get(username=request.user.username)
        links = ShortLink.objects.filter(user=user)
        context = {'links': links, 'user': user}
        return render(request, 'list_links.html', context)
