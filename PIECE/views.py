from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from .forms import EspeciesForm, PlantasForm, MineraisForm,EstacaoForm,PHform,soloForm,IrrigacaoForm,SolForm,CadastroEspecieMineralForm, RegistrationForm, LoginForm
from .models import Especies, EspeciesMinerais,Estacao,ExposicaoSolar,Solo,Irrigacao,PH,Minerais
from django.http import HttpResponse
from datetime import datetime

def Theme():
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
    
    return theme
    
    

def homepage(request):
    theme = Theme()
    especies = Especies.objects.all()


    return render(request, 'index.html', {'especies': especies ,'theme': theme})
def Cad(request):
    theme = Theme()
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
    theme = Theme()
    if request.method == 'POST':
        form = MineraisForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Cadastro de minerio')
    else:
        form = MineraisForm()
    return render(request, 'cadastrominerais.html', {'form': form, 'theme': theme})

def Cadest(request):
    theme = Theme()
    if request.method == 'POST':
        form = EstacaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Cadastro de estacao')
    else:
        form = EstacaoForm()
    return render(request, 'cadastroestacao.html', {'form': form, 'theme': theme})

def CadSolo(request):
    theme = Theme()
    if request.method == 'POST':
        form = soloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Cadastro de solo')
    else:
        form = soloForm()
    return render(request, 'cadastrosolo.html', {'form': form, 'theme': theme})

def CadSol(request):
    theme = Theme()
    if request.method == 'POST':
        form = SolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Cadastro de sol')
    else:
        form = SolForm()
    return render(request, 'cadastroSol.html', {'form': form, 'theme': theme})

def CadPH(request):
    theme = Theme()
    if request.method == 'POST':
        form = PHform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Cadastro de ph')
    else:
        form = PHform()
    return render(request, 'cadastroph.html', {'form': form, 'theme': theme})

def Cadirriga(request):
    theme = Theme()
    if request.method == 'POST':
        form = IrrigacaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Cadastro de irrigacao')
    else:
        form = IrrigacaoForm()
    return render(request, 'cadastroIrrigacao.html', {'form': form, 'theme': theme})

def Cadminesp(request):
    theme = Theme()
    minerais = Minerais.objects.all()
    especies = Especies.objects.all()

     
    if request.method == 'POST':
        form = CadastroEspecieMineralForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)  # Adicionando o argumento commit=True
            return redirect('Cadastro de Espmin')
    else:
        form = CadastroEspecieMineralForm()
    

    
    return render(request, 'cadastroespecieminerio.html', {'especies': especies, 'minerais': minerais,'theme': theme, 'form': form })

def buscar_especie(request):
    especies = Especies.objects.all()
    return render(request, 'buscarespe.html', {'especies': Especies})

def perfil_especie(request, pk):
    especie = get_object_or_404(Especies, pk=pk)
    minerais = especie.especiesminerais_set.all()
    theme = Theme()
    return render(request, 'base_perfil_especies.html', {'theme': theme, 'especie': especie, 'minerais': minerais})
    
def register(request):
    theme = Theme()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'theme': theme, 'form': form})

def login(request):
    theme = Theme()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                auth_login(request, user)
                return redirect('homepage')
            else:
                form.add_error(None, 'Credenciais inválidas.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'theme': theme, 'form': form})