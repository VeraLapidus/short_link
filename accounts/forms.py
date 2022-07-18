from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .models import CustomUser


class LoginForm(forms.Form):
    """ класс авторизации пользователя """

    username = forms.CharField(label='Логин', max_length=100)
    password = forms.CharField(label='Пароль', max_length=100, widget=forms.PasswordInput())


class CustomUserRegisterForm(forms.ModelForm):
    """ класс регистрации пользователя """

    # email = forms.EmailField(required=True, label="Адрес электронной почты")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Пароль",
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(widget=forms.PasswordInput, label="Повторите пароль",
                                help_text="введите пароль еще раз")

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Введенные пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']
