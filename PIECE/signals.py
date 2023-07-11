from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Count

from .models import Especies, Minerais,Estacao,Solo,PH,Irrigacao,ExposicaoSolar,EspeciesMinerais,User,Manutencao,Plantas,Producao,HistoricoDatas



@receiver(post_save, sender=Manutencao)
def update_planta_fields(sender, instance, **kwargs):
    planta = instance.planta
    planta.acidez_solo = instance.ultimo_ph
    planta.solo = instance.solo_atual
    planta.exposicao_solar_atual = instance.exposicao_solar_atual
    planta.save()
############################################
