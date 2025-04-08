from django import forms
from .models import DevelopmentComment

class DevelopmentCommentForm(forms.ModelForm):
    class Meta:
        model = DevelopmentComment
        fields = ['text']