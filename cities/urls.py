from django.urls import path
from cities.views import *

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('add_city/', add_city, name='add_city'),
]