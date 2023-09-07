from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = ["О сайте", "Добавить", "Обратная связь", "Войти"]

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]
def index(request):
    realty = RealEstate.objects.all()

    context = {
        'realty': realty,
        'menu': menu,
        'title': 'Главна страница',
        'type_selected': 0, #cat_selected
    }
    return render(request, 'real_estate/index.html', context=context)

def about(request):
    return render(request, 'real_estate/about.html', {'title': 'о сайте'})

def addpage(request):
    return HttpResponse("Добавить")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_realty(request, realty_id):
    realty = get_object_or_404(RealEstate, pk=realty_id)

    context = {
        'realty': realty,
        'menu': menu,
        'title': realty.title,
        'type_selected': realty.type_id,  # cat_selected
    }
    return render(request, 'real_estate/realty.html', context=context)

def show_type(request, type_id): #show_category
    realty = RealEstate.objects.filter(type_id=type_id)

    # if len(realty) == 0:
    #     raise Http404()

    context = {
        'realty': realty,
        'menu': menu,
        'title': 'Детальная информация',
        'type_selected': type_id,  # cat_selected
    }
    return render(request, 'real_estate/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
