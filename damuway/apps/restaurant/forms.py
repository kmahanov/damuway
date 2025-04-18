from django import forms
from .models import RestaurantReview

class RestaurantFilterForm(forms.Form):
    city = forms.CharField(label='Город', required=False)
    has_kids_menu = forms.ChoiceField(
        choices=[
            ('', 'Все'),
            ('yes', 'С детским меню'),
            ('no', 'Без детского меню')
        ],
        required=False,
        label='Детское меню'
    )

class RestaurantReviewForm(forms.ModelForm):
    class Meta:
        model = RestaurantReview
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
        }
