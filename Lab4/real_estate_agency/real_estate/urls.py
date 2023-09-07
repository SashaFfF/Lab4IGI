from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('realty/<int:realty_id>/', show_realty, name='realty'),
    path('type/<int:type_id>/', show_type, name='type')
]
