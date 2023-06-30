# forms.py

from django import forms
from .models import Especies, Plantas, Minerais,Estacao,Solo,PH,Irrigacao,ExposicaoSolar,EspeciesMinerais,User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('nome', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class EspeciesForm(forms.ModelForm):
    class Meta:
        model = Especies
        fields = (
            'nome',
            'nome_cientifico',
            'necessidade_solo',
            'acidez_solo',
            'exposicao_solar',
            'estacao_producao',
            'irrigacao',
            'imagem_especie',
            'imagem_fruta',
        )

class PlantasForm(forms.ModelForm):
    class Meta:
        model = Plantas
        fields = '__all__'

class MineraisForm(forms.ModelForm):
    class Meta:
        model = Minerais
        fields = (
            'nome',
            'icon_mineral',
        )
class EstacaoForm(forms.ModelForm):
    class Meta:
        model = Estacao
        fields = (
            'nome',
            'icon_estacao',
        )
class PHform(forms.ModelForm):
    class Meta:
        model = PH
        fields = (
            'nome',
            'icon_PH',
        )
class soloForm(forms.ModelForm):
    class Meta:
        model = Solo
        fields = (
            'nome',
            'icon_solo',
        )
class IrrigacaoForm(forms.ModelForm):
    class Meta:
        model = Irrigacao
        fields = (
            'nome',
            'icon_irrigacao',
        )

class SolForm(forms.ModelForm):
    class Meta:
        model = ExposicaoSolar
        fields = (
            'nome',
            'icon_exposicaosolar',
        )
        
class CadastroEspecieMineralForm(forms.ModelForm):
    class Meta: 
        model = EspeciesMinerais
        fields = (
            'especie',
            'mineral',
            'quantidade',
        )