from django.urls import path
from .views import *

urlpatterns = [
    path('', RealEstateHome.as_view(), name='home'),
    path('about/', AboutCompany.as_view(), name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('real_estate_chart/', real_estate_chart, name='real_estate_chart'),
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
    path('positions/', ShowPositions.as_view(), name='positions'),
    path('promocodes/', ShowPromocodes.as_view(), name='promocodes'),
    path('comments/', ShowComments.as_view(), name='comments'),
    path('leave_comment/', AddComment.as_view(), name='leave_comment'),
    path('clients/', ShowClients.as_view(), name='clients'),
    path('news_view/<int:article_id>', news_view, name='news_view'),
    path('politics/', politics_view, name='politics'),
    # additional table
    path('additional_table.html/', ShowAdditionalTable.as_view(), name='additional_table'),
    #api
    # path('news/', News.as_view(), name='news'),
    # path('crypto/', Crypto.as_view(), name='crypto'),
]
