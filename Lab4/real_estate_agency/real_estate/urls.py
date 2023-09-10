from django.urls import path
from .views import *

urlpatterns = [
    path('', RealEstateHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('realty/<slug:realty_slug>/', ShowRealty.as_view(), name='realty'),
    path('type/<slug:type_slug>/', RealEstateType.as_view(), name='type')
]
