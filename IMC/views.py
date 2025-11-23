from django.shortcuts import render
from .forms import Form_IMC
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Cadastro_IMC(request):
    imc = None
    if request.method != 'POST':
        form = Form_IMC()
    else:
        form = Form_IMC(request.POST, request.FILES)
        if form.is_valid():
            altura = form.cleaned_data['altura']
            peso = form.cleaned_data['peso']
            if (altura > 0):
                imc = round(peso / (altura ** 2), 2)
                form.instance.imc = imc
                form.save()
                messages.success(request, 'Cadastro realizado com sucesso!')
            else:
                messages.error(request, 'Erro ao cadastrar. A altura deve ser um número positivo.')
            form = Form_IMC()
        else:
            messages.error(request, 'Erro ao cadastrar. Verifique os dados preenchidos.')
    context = {'form':form, 'imc':imc}
    return render(request, 'Avaliacao_IMC.html', context)