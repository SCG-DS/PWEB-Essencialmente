from django.shortcuts import render
from .forms import Form_IMC
from django.contrib import messages
from .models import Avaliar_IMC, classificar_imc

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Cadastro_IMC(request):
    imc = None
    classificacao = None # Variável para armazenar a classificação
    
    if request.method != 'POST':
        form = Form_IMC()
    else:
        form = Form_IMC(request.POST, request.FILES)
        if form.is_valid():
            altura = form.cleaned_data['altura']
            peso = form.cleaned_data['peso']
            
            if (altura > 0):
                imc = round(peso / (altura ** 2), 2)
                classificacao = classificar_imc(imc) # mudei pro q ta feito no models
                
                form.instance.imc = imc
                form.instance.classificacao = classificacao # adicionado a parte da classificacao la 
                
                form.save()
                
                messages.success(request, f'Cadastro realizado com sucesso! Seu IMC é {imc} ({classificacao}).')
            else:
                messages.error(request, 'Erro ao cadastrar. A altura deve ser um número positivo.')
            form = Form_IMC() 
        else:
            print(form.errors)
            messages.error(request, 'Erro ao cadastrar. Verifique os dados preenchidos.')
            
    context = {'form':form, 'imc':imc, 'classificacao': classificacao} 
    return render(request, 'Avaliacao_IMC.html', context)

def Listar_CadastradosIMC(request):
    template_name = 'ListarCadastradosIMC.html'
    
    filtro_sexo = request.GET.get('sexo')
    
    cadastros = Avaliar_IMC.objects.all().order_by('nome')
    
    if filtro_sexo and filtro_sexo != 'TODOS':
        cadastros = cadastros.filter(sexo=filtro_sexo)
        
    context = {
        'cadastros': cadastros,
        'filtro_ativo': filtro_sexo,
        'opcoes_sexo': Avaliar_IMC.SEXOS 
    }
    
    return render(request, template_name, context)
