from django import forms
from .models import Avaliar_IMC

class Form_IMC(forms.ModelForm):
    #Aparece no formato certo dos negocio ai
    altura = forms.DecimalField(
        label='Altura (m)',
        max_digits=4,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'step': '0.01',
            'placeholder': 'Ex: 1.70',
            'min': '0.50',
            'max': '2.50'
        })
    )
    
    peso = forms.DecimalField(
        label='Peso (kg)',
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'step': '0.1',
            'placeholder': 'Ex: 70.5',
            'min': '10',
            'max': '300'
        })
    )
    
    class Meta:
        model = Avaliar_IMC
        fields = '__all__'
        widgets = {
            'dataNascimento': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'dd/mm/aaaa'
            }),
            'cpf': forms.TextInput(attrs={
                'placeholder': 'Somente números'
            }),
            'nome': forms.TextInput(attrs={
                'placeholder': 'Nome completo'
            }),
            'escola': forms.TextInput(attrs={
                'placeholder': 'Nome da escola'
            })
        }