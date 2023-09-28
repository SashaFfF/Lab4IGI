from .models import *
import requests

menu = [{'title': "Главная", 'url_name': 'mainpage'},
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Сделки", 'url_name': 'deals'},
        {'title': "Сотрудники", 'url_name': 'employees'},
        {'title': "Клиенты", 'url_name': 'clients'},
        #  {'title': "Мировые новости", 'url_name': 'news'},
        # {'title': "Курс Биткоина", 'url_name': 'crypto'},
        ]

class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        types = PropertyType.objects.all()

        user_menu = menu.copy()

        #api
        # url_news = "https://newsapi.org/v2/top-headlines?country=us&apiKey=8c41bbbc22144f9ba156f765d9c0d67c"
        # response_news = requests.get(url_news)
        # data_news = response_news.json()
        # articles = data_news["articles"]
        #
        # url_crypto = "https://rest.coinapi.io/v1/exchangerate/BTC/USD"
        # headers = {"X-CoinAPI-Key": "6A9F2F49-2DE5-4763-A187-CBD7C4700939"}
        # response_crypto = requests.get(url_crypto, headers=headers)
        # data_crypto = response_crypto.json()
        # rate = data_crypto["rate"]
        #api

        if not self.request.user.is_authenticated:
            user_menu.pop(2)
            user_menu.pop(3)

        context['menu'] = user_menu

        context['types'] = types

        #api
        # context['rate'] = rate
        # context['articles'] = articles
        #api

        if 'type_selected' not in context:
            context['type_selected'] = 0
        return context
