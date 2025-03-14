from django import forms
from .models import Plainte

class PlainteForm(forms.ModelForm):
    class Meta:
        model = Plainte
        fields = ['titre', 'description','categorie','statut']