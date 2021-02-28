from django import forms
from cities.models import City

class RoutesForm(forms.Form):
    from_city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control js-example-basic-single',
    }), label='Откуда')
    to_city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control js-example-basic-single',
    }), label='Куда')
    cities = forms.ModelMultipleChoiceField(
        queryset=City.objects.all(),
        label='Через города',
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control js-example-basic-multiple',
        })
    )
    travelling_time = forms.IntegerField(label='Время в пути', widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Время в пути'
        }
    ))
