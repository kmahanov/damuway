from django import forms
from .models import SportsClubReview
from .models import SPORT_TYPES

class SportsClubReviewForm(forms.ModelForm):
    class Meta:
        model = SportsClubReview
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Напишите ваш отзыв...'}),
        }
        labels = {
            'rating': 'Оценка',
            'comment': 'Комментарий',
        }

class SportsClubFilterForm(forms.Form):
    city = forms.CharField(label='Город', required=False)
    sport_type = forms.ChoiceField(
        choices=[('', 'Все виды спорта')] + SPORT_TYPES,
        required=False,
        label='Вид спорта'
    )