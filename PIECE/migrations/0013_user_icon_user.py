# Generated by Django 4.2 on 2023-06-30 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PIECE', '0012_user_alter_especiesminerais_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='icon_user',
            field=models.ImageField(null=True, upload_to='imagens/icon_user/'),
        ),
    ]
