from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from OnlineShop.models import Card, Comment


class FormCard(forms.ModelForm):

    class Meta:
        model = Card
        fields = [
            'number',
            'name',
            'month',
            'year',
            'cvc',
        ]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

class CreateComs(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {
            'text',
        }