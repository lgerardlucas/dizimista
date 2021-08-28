from django import forms
from .models import Comunidade

class ComunidadeForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
    #    super(Comunidade, self).__init__(*args, **kwargs)

    class Meta:
        model = Comunidade
        fields = ('__all__')
