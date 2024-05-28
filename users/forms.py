from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from dogs.forms import StyleFormMixin
from users.models import User
from django import forms


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',  'phone', 'telegram', 'avatar')


class UserPofileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'telegram', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
