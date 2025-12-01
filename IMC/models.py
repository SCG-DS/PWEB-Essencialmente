from django.db import models
from stdimage import StdImageField

# Create your models here.
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
    altura = models.FloatField('Altura', null=False, blank=False)
    peso = models.FloatField('Peso', null=False, blank=False)
    foto = StdImageField('Foto', upload_to='fotos', null=False, blank=False, default='fotos/sem_foto.png', variations={'thumb':(125, 125)})
    imc = models.FloatField('IMC', null=True, blank=True)
