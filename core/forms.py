from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from core.models import User


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password')


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields
