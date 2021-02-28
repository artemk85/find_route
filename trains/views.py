from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from trains.forms import TrainsForm
from trains.models import Train

# def home(request):
#     form = TrainsForm()
#     list_trains = Train.objects.order_by('name')
#     lst = Paginator(list_trains, 2)
#     page_number = request.GET.get('page')
#     page_obj = lst.get_page(page_number)
#     context = {'page_obj': page_obj, 'form': form }
#     return render(request, 'trains/home.html', context)

class TrainsDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'

class TrainsCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainsForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Поезд успешно создан."

class TrainsUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainsForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Поезд успешно изменен."

class TrainsDeleteView(SuccessMessageMixin, DeleteView):
    model = Train
    #template_name = 'trains/delete.html'
    success_url = reverse_lazy('trains:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Поезд успешно удален.')
        return self.post(request, *args, **kwargs)

class TrainsListView(ListView):
    paginate_by = 5
    model = Train
    template_name = 'trains/home.html'