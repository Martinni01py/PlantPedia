# forms.py

from django import forms
from .models import Especies, Minerais,Estacao,Solo,PH,Irrigacao,ExposicaoSolar,EspeciesMinerais,User,Manutencao,Plantas,Producao
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
class ManutencaoForm(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = ['dt_ultima_fertilizacao', 'ultima_medicao_ph', 'dt_ultima_poda','ultimo_ph','solo_atual','exposicao_solar_atual','planta']
class ProducaoForm(forms.ModelForm):
    class Meta:
        model = Producao
        fields = ['planta', 'dt_ultima_producao','estacao_ultima_producao']    
class PlantasForm(forms.ModelForm):
    class Meta:
        model = Plantas
        fields = '__all__'
        widgets = {
            'dt_plantio': forms.DateInput(attrs={'class': 'input', 'placeholder': 'Data de Plantio'}),
            }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # obtém o usuário passado como argumento
        super().__init__(*args, **kwargs)
        if user:
            self.fields['usuario'].initial = user  # define o usuário como valor inicial do campo

