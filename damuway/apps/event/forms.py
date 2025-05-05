from django import forms
from .models import Event

class EventFilterForm(forms.Form):
    category = forms.ChoiceField(
        choices=[('', 'Все категории')] + Event.CATEGORY_CHOICES,
        required=False
    )
    search = forms.CharField(required=False, label='Поиск')
    date = forms.DateField(required=False, widget=forms.HiddenInput())
