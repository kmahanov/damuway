from django import forms
from .models import  Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['value']
        widgets = {
            'value': forms.Select(attrs={'class': 'form-control'}, choices=[(i, i) for i in range(1, 6)])
        }
