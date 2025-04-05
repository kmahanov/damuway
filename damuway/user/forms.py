from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
import re

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) > 150:
            raise forms.ValidationError("Имя пользователя не должно превышать 150 символов.")

        if not re.match(r'^[\w@./+-_]+$', username):
            raise forms.ValidationError("Имя пользователя может содержать только буквы, цифры и символы @/./+/-/_.")

        return username


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
