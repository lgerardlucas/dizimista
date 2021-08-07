from django import forms
from .models import Paroquia

class ParoquiaForm(forms.ModelForm):
    class Meta:
        model = Paroquia

        fields = ('__all__')
  