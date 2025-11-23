from django import forms
from .models import Avaliar_IMC

class Form_IMC(forms.ModelForm):
    class Meta:
        model = Avaliar_IMC
        fields = ['cpf', 'nome', 'sexo', 'dataNascimento', 'escola', 'altura', 'peso', 'foto']