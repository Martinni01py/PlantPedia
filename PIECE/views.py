from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.db import transaction
from .forms import EspeciesForm, MineraisForm,EstacaoForm,PHform,soloForm,IrrigacaoForm,SolForm,CadastroEspecieMineralForm, RegistrationForm, LoginForm,MineraisForm,PlantasForm,ManutencaoForm,ProducaoForm
from .models import Especies, EspeciesMinerais,Estacao,ExposicaoSolar,Solo,Irrigacao,PH,Minerais,Plantas,HistoricoDatas,Producao,Manutencao
from django.contrib.auth.decorators import login_required
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
    
    
##PagInicial
def homepage(request):
    theme = Theme()
    especies = Especies.objects.all()


    return render(request, 'index.html', {'especies': especies ,'theme': theme})
##Cadastro Especie
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
##Cadastro minerios
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
##Cadastro estação
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
##Cadastro solo
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
##Cadastro sol
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
##Cadastro PH
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
##Cadastro irrigação
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
##Cadastro minerios da espécie
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

##perfil espécie#
def perfil_especie(request, pk):
    especie = get_object_or_404(Especies, pk=pk)
    minerais = especie.especiesminerais_set.all()
    theme = Theme()
    return render(request, 'base_perfil_especies.html', {'theme': theme, 'especie': especie, 'minerais': minerais})

##plantas perfil
@login_required    
def perfil_planta(request, pk):
    planta = get_object_or_404(Plantas, pk=pk)
    especie = get_object_or_404(Especies, pk=planta.especie.id)
    minerais = especie.especiesminerais_set.all()
    estacoes = Estacao.objects.all()
    solos = Solo.objects.all()
    exposicaoSolar = ExposicaoSolar.objects.all()
    irrigacoes = Irrigacao.objects.all()
    phs = PH.objects.all()
    historicos = HistoricoDatas.objects.all()
    producao = Producao.objects.all()
    manutencao = Manutencao.objects.all()

    
    if request.method == 'POST':
        form1 = ManutencaoForm(request.POST, request.FILES)
        form2 = ProducaoForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save(commit=True)  # Adicionando o argumento commit=True

        elif form2.is_valid():
            form2.save(commit=True)  # Adicionando o argumento commit=True
            
    else:
        form1 = ManutencaoForm()
        form2 = ProducaoForm()
    
    theme = Theme()
    return render(request, 'homepage2.html', {'planta': planta,'phs': phs, 'solos': solos, 'exposicaoSolar': exposicaoSolar, 'irrigacoes': irrigacoes, 'estacoes': estacoes, 'theme': theme, 'especie': especie, 'minerais': minerais, 'historicos': historicos,'manutencao':manutencao,'producao':producao, 'form1': form1, 'form2': form2})

##galeria plantas
@login_required
def galeria_plantas(request):
    plantas = Plantas.objects.filter(usuario=request.user)
    especie = Especies.objects.all()
    user = request.user
    
    theme = Theme()
    return render(request, 'plantas.html', {'user': user,'theme': theme, 'especie': especie, 'plantas': plantas})

##cadastro plantas
@login_required
def CadPlanta(request):
    theme = Theme()
    estacoes = Estacao.objects.all()
    solos = Solo.objects.all()
    exposicaoSolar = ExposicaoSolar.objects.all()
    especies = Especies.objects.all()
    irrigacoes = Irrigacao.objects.all()
    phs = PH.objects.all()
    user = request.user
    if request.method == 'POST':
        form = PlantasForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('Plantas')
    else:
        form = PlantasForm(user=request.user)
    return render(request, 'cadastroPlanta.html', {'user': user,'especies': especies, 'phs': phs, 'solos': solos, 'exposicaoSolar': exposicaoSolar, 'irrigacoes': irrigacoes, 'estacoes': estacoes, 'theme': theme, 'form': form })
 
##registro
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
##login
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


