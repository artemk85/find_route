from django.contrib import messages
from django.shortcuts import render
from routes.forms import RoutesForm

# Create your views here.
from routes.utils import get_routes


def home(request):
    form = RoutesForm()
    return render(request, 'routes/home.html', {'form': form})

def find_routes(request):
    if request.method == 'POST':
        form = RoutesForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/home.html', {'form': form})
            return render(request, 'routes/home.html', context)
        return render(request, 'routes/home.html', {'form': form})
    else:
        form = RoutesForm()
        messages.error(request,'Нет данных для поиска !')
        return render(request, 'routes/home.html', {'form': form})
