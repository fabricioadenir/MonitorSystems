from django import forms
from .models import DataBases, User


class BaseDeDadosForm(forms.ModelForm):
    class Meta:
        model = DataBases
        fields = ('__all__')
        widgets = {
            'password': forms.PasswordInput(),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('__all__')
        widgets = {
            'password': forms.PasswordInput(),
        }
