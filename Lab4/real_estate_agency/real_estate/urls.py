from django.urls import path
from .views import *

urlpatterns = [
    path('', RealEstateHome.as_view(), name='home'),
    path('about/', AboutCompany.as_view(), name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('deals/', ShowDeals.as_view(), name='deals'),
    path('realty/<slug:realty_slug>/', ShowRealty.as_view(), name='realty'),
    path('type/<slug:type_slug>/', RealEstateType.as_view(), name='type'),
    path('mainpage/', MainPage.as_view(), name='mainpage'),
    path('sertificate/', Sertificate.as_view(), name='sertificate'),
    path('employees/', ShowEmployees.as_view(), name='employees'),
    path('articles/', ShowArticles.as_view(), name='articles'),
    path('questions/', ShowQuestions.as_view(), name='questions'),
]
