from django import forms
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        try:
            self.user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(f'Пользователь с логином "{username}" не найден !')

        if not self.user.check_password(password):
            raise forms.ValidationError(f'Пароль для пользователя "{username}" не верный !')

        return cleaned_data
