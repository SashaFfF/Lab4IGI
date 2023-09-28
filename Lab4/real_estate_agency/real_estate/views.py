from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, TemplateView, FormView
from .utils import *
import numpy as np
from matplotlib import pyplot as plt
# from qsstats import QuerySetStats


class RealEstateHome(DataMixin, ListView):
    model = RealEstate
    template_name = 'real_estate/index.html'
    context_object_name = 'realty'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Недвижимость")
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return RealEstate.objects.filter(purchased=True)


class ShowDeals(DataMixin, ListView):
    model = Deal
    template_name = 'real_estate/deals.html'
    context_object_name = 'deals'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Оформленные договоры")
        return dict(list(context.items()) + list(c_def.items()))


    def get_queryset(self):
        return Deal.objects.all()


def generate_chart(request):
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        plt.plot(x, y)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('График')

        # Сохранение графика как изображения
        plt.savefig('chart.png')

        return render(request, 'chart.html')

# def view_func(request):
#         start_date = ...
#         end_date = ...
#
#         queryset = RealEstate.objects.all()
#         # считаем количество платежей...
#         qsstats = QuerySetStats(queryset, date_field='datetime', aggregate=Count('id'))
#         # ...в день за указанный период
#         values = qsstats.time_series(start_date, end_date, interval='days')
#
#         return render('chart.html', {'values': values})

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

# def about(request):
#     return render(request, 'real_estate/Lab1/about.html', {'title': 'о сайте'})

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddDealForm
    template_name = 'real_estate/addpage.html'
    success_url = reverse_lazy('deals')
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


# Lab1

class MainPage(DataMixin, ListView):
    model = RealEstate
    template_name = 'real_estate/Lab1/mainpage.html'
    context_object_name = 'realty'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return RealEstate.objects.filter(purchased=True).order_by('-time_create')[:1]


class AboutCompany(DataMixin, ListView):
    model = RealEstate
    template_name = 'real_estate/Lab1/about.html'
    context_object_name = 'realty'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="О компании")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return RealEstate.objects.filter(purchased=True)


class Sertificate(DataMixin, TemplateView):
    template_name = 'real_estate/Lab1/sertificate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Сертификат')

        return dict(list(context.items()) + list(c_def.items()))


class ShowEmployees (DataMixin, ListView):
    model = Employee
    template_name = 'real_estate/Lab1/employees.html'
    context_object_name = 'employees'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Сотрудники")
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Employee.objects.all()


class ShowArticles (DataMixin, ListView):
    model = Article
    template_name = 'real_estate/Lab1/articles.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Статьи")
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Article.objects.all()


class ShowQuestions (DataMixin, ListView):
    model = Question
    template_name = 'real_estate/Lab1/questions.html'
    context_object_name = 'questions'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Вопросы")
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Question.objects.all()


class ShowPositions (DataMixin, ListView):
    model = Position
    template_name = 'real_estate/Lab1/positions.html'
    context_object_name = 'positions'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Список вакансий")
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Position.objects.filter(is_vacant=True)


class ShowPromocodes (DataMixin, ListView):
    model = PromotionalCode
    template_name = 'real_estate/Lab1/promocodes.html'
    context_object_name = 'promocodes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Промокоды")
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return PromotionalCode.objects.all()


class ShowComments (DataMixin, ListView):
    model = Comment
    template_name = 'real_estate/Lab1/comments.html'
    context_object_name = 'comments'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Отзывы")
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Comment.objects.all()


# class LeaveComment(LoginRequiredMixin, DataMixin, CreateView):
#     form_class = CommentForm
#     template_name = 'real_estate/Lab1/leave_comment.html'
#     success_url = reverse_lazy('comments')
#     login_url = reverse_lazy('home') # указывает адрес перенаправления для неавторизированного пользователя
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Оставить отзыв")
#         return dict(list(context.items()) + list(c_def.items()))


class AddComment(LoginRequiredMixin, DataMixin, FormView):
    template_name = 'real_estate/Lab1/leave_comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('comments')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Оставить отзыв")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        form.instance.name = self.request.user.username
        form.save()
        return super().form_valid(form)


class ShowClients (DataMixin, ListView):
    model = Client
    template_name = 'real_estate/clients.html'
    context_object_name = 'clients'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Клиенты")
        return dict(list(context.items())+list(c_def.items()))

    def get_queryset(self):
        return Client.objects.all()


#API
# class News(DataMixin, ListView):
#     model = RealEstate
#     template_name = 'real_estate/api/news.html'
#     context_object_name = 'posts'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Мировые новости')
#
#         return dict(list(context.items()) + list(c_def.items()))
#
#
# class Crypto(DataMixin, ListView):
#     model = RealEstate
#     template_name = 'real_estate/api/crypto.html'
#     context_object_name = 'posts'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Курс биткоина')
#
#         return dict(list(context.items()) + list(c_def.items()))



def news_view(request, article_id):
    article = Article.objects.all()
    pushcase = Article.objects.get(pk=article_id)

    context = {
        'article': article,
        'pushcase': pushcase
    }
    return render(request, 'real_estate/Lab1/news_view.html', context)

def politics_view(request):
    return render(request, 'real_estate/Lab1/politics.html')

def real_estate_chart(request):
    # Получите данные из модели RealEstate
    data = RealEstate.objects.all()

    # Пример: Создайте диаграмму распределения типов недвижимости
    property_types = PropertyType.objects.annotate(
        count=Count('realestate')
    ).values('type', 'count')

    labels = [item['type'] for item in property_types]
    counts = [item['count'] for item in property_types]

    # Создайте график
    plt.figure(figsize=(10, 6))
    plt.bar(labels, counts)
    plt.xlabel('Тип недвижимости')
    plt.ylabel('Количество')
    plt.title('Распределение типов недвижимости')

    # Сохраните график в формате PNG
    chart_path = 'real_estate/static/real_estate/images/real_estate_chart.png'
    plt.savefig(chart_path)

    return render(request, 'real_estate/chart.html', {'chart_path': chart_path})



