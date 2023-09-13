from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить", 'url_name': 'add_page'},
        {'title': "Сделки", 'url_name': 'deals'},
        {'title': "Обратная связь", 'url_name': 'contact'},

        ]

class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        types = PropertyType.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
            user_menu.pop(1)

        context['menu'] = user_menu

        context['types'] = types
        if 'type_selected' not in context:
            context['type_selected'] = 0
        return context
