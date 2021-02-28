from django import forms
from trains.models import Train
from cities.models import City


class TrainsForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите номер поезда'
    }), label='№ Поезда')
    from_city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }), label='Откуда')
    to_city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }), label='Куда')
    travel_time = forms.IntegerField(label='Время в пути', widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Время в пути'
        }
    ))

    class Meta:
        model = Train
        fields = '__all__'
