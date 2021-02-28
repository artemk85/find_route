from django.urls import path
from trains.views import *

urlpatterns = [
    path('', TrainsListView.as_view(), name='home'),
    path('detail/<int:pk>/', TrainsDetailView.as_view(), name='detail'),
    path('add/', TrainsCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', TrainsUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', TrainsDeleteView.as_view(), name='delete'),
]