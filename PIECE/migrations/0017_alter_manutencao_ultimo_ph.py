# Generated by Django 4.2 on 2023-06-30 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PIECE', '0016_rename_exposicao_solar_plantas_exposicao_solar_atual_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manutencao',
            name='ultimo_ph',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PIECE.ph'),
        ),
    ]
