from django import forms
from .models import KindergartenReview, Kindergarten
from ..school.models import District


class KindergartenReviewForm(forms.ModelForm):
    class Meta:
        model = KindergartenReview
        fields = ['text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Ваш отзыв...'}),
            'rating': forms.Select()
        }

class KindergartenSearchForm(forms.Form):
    district = forms.ModelChoiceField(queryset=District.objects.all(), required=False, label='Район')
    kindergarten_type = forms.ChoiceField(choices=[('', 'Тип')]+list(Kindergarten.KINDERGARTEN_TYPES), required=False)
    min_rating = forms.IntegerField(min_value=1, max_value=5, required=False, label='Минимальный рейтинг')
