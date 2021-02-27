from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from cities.forms import HtmlForm, CityForm
from cities.models import City

__all__ = (
    'home',
    'CityDetailView',
    'add_city',
)


def index(request):
    return render(request, 'home.html', {'cities': "Moscow"})


def home(request):
    form = HtmlForm()
    list_cities = City.objects.all()
    context = {'objects_list': list_cities, 'form': form}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


def add_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('cities:home')
