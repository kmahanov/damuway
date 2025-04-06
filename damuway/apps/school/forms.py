from django import forms
from .models import Review, School, District

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
        }

class SchoolSearchForm(forms.Form):
    district = forms.ModelChoiceField(
        queryset=District.objects.all(),
        required=False,
        label="Район",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    school_type = forms.ChoiceField(
        choices=School.SCHOOL_TYPES,
        required=False,
        label="Тип школы",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    min_rating = forms.IntegerField(
        required=False,
        label="Минимальный рейтинг",
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1-5'})
    )