from django import forms
from .models import Ofertante

class OfertanteForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
    #    super(Comunidade, self).__init__(*args, **kwargs)

    class Meta:
        model = Ofertante
        fields = ('__all__')
