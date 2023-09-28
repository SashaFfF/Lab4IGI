from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import request

from .models import *

class AddDealForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)
        self.fields['owner'].empty_label = "Не выбран"
        self.fields['agent'].empty_label = "Не выбран"
        self.fields['buyer'].empty_label = "Не выбран"

    def clean_age(self):
        age = self.cleaned_data['age']

        if age < 18:
            raise ValidationError('Вы должны быть старше 18 лет для заключения сделки.')

        return age

    class Meta:
        model = Deal
        fields = ['real_estate', 'owner', 'buyer', 'age','agent'] #позже убрать агента
        #fields = '__all__'


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = '__all__'


class CommentForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)

    class Meta:
        model = Comment
        fields = ['comment', 'grade']
        widgets = {
            'comment': forms.Textarea(),
            'grade': forms.NumberInput(),
        }