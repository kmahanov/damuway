from django import forms
from .models import ClubReview

class ClubFilterForm(forms.Form):
    city = forms.CharField(required=False, label='Город')
    search = forms.CharField(required=False, label='Название кружка')

class ClubReviewForm(forms.ModelForm):
    class Meta:
        model = ClubReview
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, f"{i} ★") for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
