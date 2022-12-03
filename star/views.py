import pygsheets
import datetime
from django.shortcuts import render
from django.views.generic import DetailView

from main.settings import BASE_DIR

from .models import *


def home(request):
    star = StarProfile.objects.all()
    popular_stars = StarProfile.objects.filter(popular=True).order_by('star_id')
    category = StarCategory.objects.all()
    cat1 = StarCategory.objects.get(id=1)
    cat2 = StarCategory.objects.get(id=2)
    cat3 = StarCategory.objects.get(id=3)

    context = {'stars': star, 'popular_stars': popular_stars, 'category': category, 'cat1': cat1, 'cat2': cat2,
               'cat3': cat3}
    return render(request, 'home.html', context)


def congratulations(request):
    star = StarProfile.objects.all()
    category = StarCategory.objects.all()
    cat1 = StarCategory.objects.get(id=1)
    cat2 = StarCategory.objects.get(id=2)
    cat3 = StarCategory.objects.get(id=3)

    context = {'stars': star, 'category': category, 'cat1': cat1, 'cat2': cat2,
               'cat3': cat3}
    return render(request, 'congratulations/congratulations.html', context)


class CongratulationsDetailView(DetailView):
    model = StarProfile
    template_name = 'congratulations/congratulations-detail.html'
    context_object_name = 'congratulations'
    pk_url_kwarg = 'congratulations_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


def stars(request):
    return render(request, 'stars/stars.html')


def toasts(request):
    toast = Toasts.objects.all()
    category = ToastsCategory.objects.all()
    context = {'toast': toast, 'category': category}
    return render(request, 'toasts/toasts.html', context)


def contacts(request):
    return render(request, 'contacts/contacts.html')

def tel_bot(request):
    gc = pygsheets.authorize(service_file=f'{BASE_DIR}/star/creds.json')
    sh = gc.open_by_url(
        'https://docs.google.com/spreadsheets/d/1SmBSeig_GSEftIT6Zpqx8dhWP4Bf7CjVnb0VJw48feY/edit#gid=367067341')
    sheet = sh.sheet1
    context = {'result': sheet.rows, 'time': datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}
    return render(request, 'bot/bot.html', context)

