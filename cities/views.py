from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from cities.forms import HtmlForm, CityForm
from cities.models import City



def index(request):
    return render(request, 'home.html', {'cities': "Moscow"})


def home(request):
    form = CityForm()
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

class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')

class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
