from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import BooleanField

from users.models import User


class StyleFormMixin:
    """Миксин для стилизации форм"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Форма для регистрации пользователя"""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].help_text = forms.HiddenInput()
        self.fields['password2'].help_text = forms.HiddenInput()


class UserProfileForm(StyleFormMixin, UserChangeForm):
    """Модель для настройки профиля пользователя"""
    class Meta:
        model = User
        fields = ('username', 'email', 'avatar',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
