from django import forms
from .models import ParentReview

class ParentReviewForm(forms.ModelForm):
    class Meta:
        model = ParentReview
        fields = ['rating', 'comment']