from django.urls import path

from .views import start_page, short_link, revers_transformation, list_links

app_name = 'main'
urlpatterns = [
    path('', start_page, name='start_page'),
    path('short_link/', short_link, name='short_link'),
    path('<slug:slug>', revers_transformation, name='revers_transformation'),
    path('list_links/', list_links, name='list_links'),

]
