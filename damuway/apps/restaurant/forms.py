from django import forms
from .models import Restaurant

class RestaurantFilterForm(forms.Form):
    city = forms.CharField(required=False, label='Город')
    search = forms.CharField(required=False, label='Поиск по названию')

from .models import RestaurantReview

class ReviewForm(forms.ModelForm):
    class Meta:
        model = RestaurantReview
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, f"{i} ★") for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
