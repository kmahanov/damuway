from django import forms
from .models import Review, School

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
        }

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'
        widgets = {
            'latitude': forms.NumberInput(attrs={'step': "0.000001"}),
            'longitude': forms.NumberInput(attrs={'step': "0.000001"}),
        }