from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CommentForm(forms.Form):
    comment = forms.CharField(
        label="",
        widget=forms.Textarea
    )

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))

    class Meta:
        model = User
        fields = {'username', 'password1', 'password2'}
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-input'}),
            'password1' : forms.PasswordInput(attrs={'class':'form-input'}),
            'password2' : forms.PasswordInput(attrs={'class':'form-input'}),
        }

# class LoginUserForm

class SearchForm(forms.Form):
    searchLine = forms.CharField(label="Поиск", widget=forms.TextInput(attrs={'class' : 'form-input'}))
