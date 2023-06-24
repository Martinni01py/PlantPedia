# forms.py

from django import forms
from .models import Especies, Plantas, Minerais,Estacao,Solo,PH,Irrigacao,ExposicaoSolar

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
        
class CadastroEspecieMineralForm(forms.Form):
    especie = forms.ModelChoiceField(queryset=Especies.objects.all())
    mineral = forms.ModelChoiceField(queryset=Minerais.objects.all())
    quantidade = forms.DecimalField()

    def save(self):
        especie = self.cleaned_data['especie']
        mineral = self.cleaned_data['mineral']
        quantidade = self.cleaned_data['quantidade']