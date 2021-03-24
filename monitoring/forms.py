from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import DataBases, Profile


class BaseDeDadosForm(forms.ModelForm):
    class Meta:
        model = DataBases
        fields = ('__all__')
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileForm(UserCreationForm):
    model = Profile
    fields = "__all__"
