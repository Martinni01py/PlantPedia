from django.shortcuts import render, redirect, get_object_or_404
from .forms import EspeciesForm, PlantasForm, MineraisForm,EstacaoForm,PHform,soloForm,IrrigacaoForm,SolForm
from .models import Especies, EspeciesMinerais,Estacao,ExposicaoSolar,Solo,Irrigacao,PH
from django.http import HttpResponse
from datetime import datetime

def homepage(request):
    current_datetime = datetime.now()
    current_month = current_datetime.month

    # Determinar a estação com base no mês atual
    if current_month in [6, 7, 8, 9]:  # Inverno 
        theme = 'inverno.css'
    elif current_month in [10, 11,12]:  # Primavera 
        theme = 'primavera.css'
    elif current_month in [1, 2, 3]:  # Verão 
        theme = 'verao.css'
    else:  # Outono 
        theme = 'outono.css'

    return render(request, 'index.html', {'theme': theme})
def Cad(request):
    current_datetime = datetime.now()
    current_month = current_datetime.month

    # Determinar a estação com base no mês atual
    if current_month in [6, 7, 8, 9]:  # Inverno 
        theme = 'inverno.css'
    elif current_month in [10, 11,12]:  # Primavera 
        theme = 'primavera.css'
    elif current_month in [1, 2, 3]:  # Verão 
        theme = 'verao.css'
    else:  # Outono 
        theme = 'outono.css'
    estacoes = Estacao.objects.all()
    solos = Solo.objects.all()
    exposicaoSolar = ExposicaoSolar.objects.all()
    irrigacoes = Irrigacao.objects.all()
    phs = PH.objects.all()
    

    
    if request.method == 'POST':
        form = EspeciesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)  # Adicionando o argumento commit=True
            return redirect('Cadastro de Espécie')
    else:
        form = EspeciesForm()
    

    
    return render(request, 'cadastroespecie.html', {'phs': phs, 'solos': solos, 'exposicaoSolar': exposicaoSolar, 'irrigacoes': irrigacoes, 'estacoes': estacoes, 'theme': theme, 'form': form })

def Cadmin(request):
    current_datetime = datetime.now()
    current_month = current_datetime.month

    # Determinar a estação com base no mês atual
    if current_month in [6, 7, 8, 9]:  # Inverno 
        theme = 'inverno.css'
    elif current_month in [10, 11,12]:  # Primavera 
        theme = 'primavera.css'
    elif current_month in [1, 2, 3]:  # Verão 
        theme = 'verao.css'
    else:  # Outono 
        theme = 'outono.css'
    if request.method == 'POST':
        form = MineraisForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Cadastro de minerio')
    else:
        form = MineraisForm()
    return render(request, 'cadastrominerais.html', {'form': form, 'theme': theme})

def Cadest(request):
    current_datetime = datetime.now()
    current_month = current_datetime.month

    # Determinar a estação com base no mês atual
    if current_month in [6, 7, 8, 9]:  # Inverno 
        theme = 'inverno.css'
    elif current_month in [10, 11,12]:  # Primavera 
        theme = 'primavera.css'
    elif current_month in [1, 2, 3]:  # Verão 
        theme = 'verao.css'
    else:  # Outono 
        theme = 'outono.css'
    if request.method == 'POST':
        form = EstacaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Cadastro de estacao')
    else:
        form = EstacaoForm()
    return render(request, 'cadastroestacao.html', {'form': form, 'theme': theme})

def CadSolo(request):
    current_datetime = datetime.now()
    current_month = current_datetime.month

    # Determinar a estação com base no mês atual
    if current_month in [6, 7, 8, 9]:  # Inverno 
        theme = 'inverno.css'
    elif current_month in [10, 11,12]:  # Primavera 
        theme = 'primavera.css'
    elif current_month in [1, 2, 3]:  # Verão 
        theme = 'verao.css'
    else:  # Outono 
        theme = 'outono.css'
    if request.method == 'POST':
        form = soloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Cadastro de solo')
    else:
        form = soloForm()
    return render(request, 'cadastrosolo.html', {'form': form, 'theme': theme})

def CadSol(request):
    current_datetime = datetime.now()
    current_month = current_datetime.month

    # Determinar a estação com base no mês atual
    if current_month in [6, 7, 8, 9]:  # Inverno 
        theme = 'inverno.css'
    elif current_month in [10, 11,12]:  # Primavera 
        theme = 'primavera.css'
    elif current_month in [1, 2, 3]:  # Verão 
        theme = 'verao.css'
    else:  # Outono 
        theme = 'outono.css'
    if request.method == 'POST':
        form = SolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Cadastro de sol')
    else:
        form = SolForm()
    return render(request, 'cadastroSol.html', {'form': form, 'theme': theme})

def CadPH(request):
    current_datetime = datetime.now()
    current_month = current_datetime.month

    # Determinar a estação com base no mês atual
    if current_month in [6, 7, 8, 9]:  # Inverno 
        theme = 'inverno.css'
    elif current_month in [10, 11,12]:  # Primavera 
        theme = 'primavera.css'
    elif current_month in [1, 2, 3]:  # Verão 
        theme = 'verao.css'
    else:  # Outono 
        theme = 'outono.css'
    if request.method == 'POST':
        form = PHform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Cadastro de ph')
    else:
        form = PHform()
    return render(request, 'cadastroph.html', {'form': form, 'theme': theme})

def Cadirriga(request):
    current_datetime = datetime.now()
    current_month = current_datetime.month

    # Determinar a estação com base no mês atual
    if current_month in [6, 7, 8, 9]:  # Inverno 
        theme = 'inverno.css'
    elif current_month in [10, 11,12]:  # Primavera 
        theme = 'primavera.css'
    elif current_month in [1, 2, 3]:  # Verão 
        theme = 'verao.css'
    else:  # Outono 
        theme = 'outono.css'
    if request.method == 'POST':
        form = IrrigacaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Cadastro de irrigacao')
    else:
        form = IrrigacaoForm()
    return render(request, 'cadastroIrrigacao.html', {'form': form, 'theme': theme})



def buscar_especie(request):
    especies = Especies.objects.all()
    return render(request, 'buscarespe.html', {'especies': Especies})

def perfil_especie(request, pk):
    especie = get_object_or_404(Especies, pk=pk)
    current_datetime = datetime.now()
    current_month = current_datetime.month

    # Determinar a estação com base no mês atual
    if current_month in [6, 7, 8, 9]:  # Inverno 
        theme = 'inverno.css'
    elif current_month in [10, 11,12]:  # Primavera 
        theme = 'primavera.css'
    elif current_month in [1, 2, 3]:  # Verão 
        theme = 'verao.css'
    else:  # Outono 
        theme = 'outono.css'
    return render(request, 'base_perfil_especies.html', {'theme': theme, 'especie': especie})
    
