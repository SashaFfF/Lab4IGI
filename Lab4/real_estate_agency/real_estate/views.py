from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from .utils import *


class RealEstateHome(DataMixin, ListView):
    model = RealEstate
    template_name = 'real_estate/index.html'
    context_object_name = 'realty'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return RealEstate.objects.filter(purchased=True)

# def index(request):
#     realty = RealEstate.objects.all()
#
#     context = {
#         'realty': realty,
#         'menu': menu,
#         'title': 'Главна страница',
#         'type_selected': 0, #cat_selected
#     }
#     return render(request, 'real_estate/index.html', context=context)

def about(request):
    return render(request, 'real_estate/about.html', {'title': 'о сайте'})

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddDealForm
    template_name = 'real_estate/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home') # указывает адрес перенаправления для неавторизированного пользователя

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Оформление сделки")
        return dict(list(context.items()) + list(c_def.items()))

# def addpage(request):
#     if request.method == 'POST':
#         form = AddDealForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка заключения сделки')
#     else:
#         form = AddDealForm()
#     return render(request, 'real_estate/addpage.html', {'form': form, 'menu': menu, 'title': 'Оформление сделки'})

def contact(request):
    return HttpResponse("Обратная связь")

# def login(request):
#     return HttpResponse("Авторизация")

class ShowRealty(DataMixin, DetailView):
    model = RealEstate
    template_name = "real_estate/realty.html"
    slug_url_kwarg = 'realty_slug'
    context_object_name = 'realty'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['realty'])
        return dict(list(context.items()) + list(c_def.items()))

# def show_realty(request, realty_slug):
#     realty = get_object_or_404(RealEstate, slug=realty_slug)
#
#     context = {
#         'realty': realty,
#         'menu': menu,
#         'title': realty.title,
#         'type_selected': realty.type_id,  # cat_selected
#     }
#     return render(request, 'real_estate/realty.html', context=context)


class RealEstateType(DataMixin, ListView):
    model = RealEstate
    template_name = 'real_estate/index.html'
    context_object_name = 'realty'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - '+str(context['realty'][0].type),
                                      type_selected=context['realty'][0].type_id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return RealEstate.objects.filter(type__slug=self.kwargs['type_slug'], purchased=True)

# def show_type(request, type_id): #show_category
#     realty = RealEstate.objects.filter(type_id=type_id)
#
#     # if len(realty) == 0:
#     #     raise Http404()
#
#     context = {
#         'realty': realty,
#         'menu': menu,
#         'title': 'Детальная информация',
#         'type_selected': type_id,  # cat_selected
#     }
#     return render(request, 'real_estate/index.html', context=context)

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'real_estate/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def=self.get_user_context(title="Регистрация")
        return dict(list(context.items())+list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'real_estate/login.html'
    # success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def=self.get_user_context(title="Авторизация")
        return dict(list(context.items())+list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
