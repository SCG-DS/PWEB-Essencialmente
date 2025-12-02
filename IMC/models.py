from django.db import models
from decimal import Decimal
from stdimage.models import StdImageField

def classificar_imc(valor_imc):
    if valor_imc is None or valor_imc == 0:
        return 'Não Calculado'
    
    if valor_imc < 18.5:
        return 'Abaixo do Normal' 
    elif valor_imc < 25.0:
        return 'Normal' 
    elif valor_imc < 30.0:
        return 'Sobrepeso' 
    elif valor_imc < 35.0:
        return 'Obesidade Grau 1'
    elif valor_imc < 40.0:
        return 'Obesidade Grau 2' 
    else:
        return 'Obesidade Grau 3'

class Avaliar_IMC(models.Model):
    SEXOS = [
        ('MASC', 'Masculino'),
        ('FEMI', 'Feminino'),
        ('NAOI', 'Não Informado')
    ]

    cpf = models.CharField('CPF', null=False, blank=False, max_length=11, unique=True, primary_key=True)
    nome = models.CharField('Nome', null=False, blank=False, max_length=70)
    sexo = models.CharField('Sexo', null=False, blank=False, max_length=9, choices=SEXOS)
    dataNascimento = models.DateField('Data de Nascimento', null=False, blank=False)
    escola = models.CharField('Escola', null=False, blank=False, max_length=100)
    altura = models.DecimalField('Altura (m)', null=False, blank=False, max_digits=4, decimal_places=2)
    peso = models.DecimalField('Peso (kg)', null=False, blank=False, max_digits=5, decimal_places=2)
    foto = StdImageField('Foto', upload_to='fotos', null=False, blank=False, default='fotos/sem_foto.png', variations={'thumb':(125, 125)})
    imc = models.DecimalField('IMC', null=True, blank=True, max_digits=5, decimal_places=2)
    classificacao = models.CharField('Classificação IMC', max_length=50, null=True, blank=True) #adicionei para facilitar a listagem

    class Meta:
        verbose_name = 'Avaliação de IMC'
        verbose_name_plural = 'Avaliações de IMC'
        
    def __str__(self):
        return self.nome
        
    def save(self, *args, **kwargs):
        """Calcula o IMC e a Classificação antes de salvar."""
        if self.altura and self.altura > 0:
            self.imc = Decimal(self.peso) / (Decimal(self.altura) ** 2)
            self.imc = round(self.imc, 2)
        else:
            self.imc = Decimal('0.0')
            
        self.classificacao = classificar_imc(float(self.imc) if self.imc else 0)
            
        super(Avaliar_IMC, self).save(*args, **kwargs)