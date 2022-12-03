from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('congratulations', congratulations, name='congratulations'),
    path('congratulations/<int:congratulations_id>/', CongratulationsDetailView.as_view(), name='congratulations'),
    path('stars', stars, name='stars'),
    path('toasts', toasts, name='toasts'),
    path('contacts', contacts, name='contacts'),
    path('za-japan', tel_bot, name='zajapan'),

]
