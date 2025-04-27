from django import forms
from .models import KindergartenReview, Kindergarten
from ..school.models import District


class KindergartenReviewForm(forms.ModelForm):
    class Meta:
        model = KindergartenReview
        fields = ['rating', 'text']
        widgets = {
            'rating': forms.Select(choices=[(i, f'{i} ★') for i in range(1, 6)], attrs={'class': 'form-select'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class KindergartenSearchForm(forms.Form):
    district = forms.ModelChoiceField(queryset=District.objects.all(), required=False, label='Район')
    kindergarten_type = forms.ChoiceField(choices=[('', 'Тип')]+list(Kindergarten.KINDERGARTEN_TYPES), required=False)
    min_rating = forms.IntegerField(min_value=1, max_value=5, required=False, label='Минимальный рейтинг')
