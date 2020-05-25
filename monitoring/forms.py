from django import forms
from .models import DataBases


class BaseDeDadosForm(forms.ModelForm):
    class Meta:
        model = DataBases
        fields = ('__all__')
        widgets = {
            'password': forms.PasswordInput(),
        }