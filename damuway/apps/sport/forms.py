from django import forms
from .models import SportsClubReview, SPORT_TYPES

class SportsClubFilterForm(forms.Form):
    city = forms.CharField(label='Город', required=False)
    sport_type = forms.ChoiceField(choices=[('', 'Все виды спорта')] + SPORT_TYPES, required=False)

class SportsClubReviewForm(forms.ModelForm):
    class Meta:
        model = SportsClubReview
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, f"{i} ★") for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
