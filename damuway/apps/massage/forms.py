from django import forms
from .models import Review, Appointment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'rating', 'comment']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['client_phone', 'date_time', 'category']
