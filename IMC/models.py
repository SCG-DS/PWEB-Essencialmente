from django.db import models
from stdimage import StdImageField

# Create your models here.
class Avaliar_IMC(models.Model):
    SEXOS = [
        ('MASC', 'Masculino'),
        ('FEMI', 'Feminino'),
        ('NAOI', 'Não Informado')
    ]

    cpf = models.CharField(verbose_name='cpf', name='cpf', null=False, blank=False, max_length=11, unique=True, primary_key=True)
    nome = models.CharField(verbose_name='Nome', name='nome', null=False, blank=False, max_length=70)
    sexo = models.CharField(verbose_name='Sexo', name='sexo', null=False, blank=False, max_length=9, choices=SEXOS)
    dataNascimento = models.DateField(verbose_name='Data de Nascimento', name='dataNascimento', null=False, blank=False)
    escola = models.CharField(verbose_name='Escola', null=False, blank=False, max_length=100)
    altura = models.FloatField(name='altura', verbose_name='Altura(cm)', null=False, blank=False)
    peso = models.FloatField(name='peso', verbose_name='Peso(kg)', null=False, blank=False)
    foto = StdImageField(name='foto', upload_to='fotos', null=False, blank=False, default='fotos/sem_foto.png', variations={'thumb':(125, 125)})
    imc = models.FloatField(name='imc', null=False, blank=False)
