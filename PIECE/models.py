from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser definido.')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    ##icon_user = models.ImageField(upload_to='imagens/icon_user/',null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    objects = UserManager()

    def __str__(self):
        return self.email



class Minerais(models.Model):
    nome = models.CharField(max_length=100)
    icon_mineral = models.ImageField(upload_to='imagens/icon_minerais/',null=True)
    def __str__(self):
        return self.nome


class Solo(models.Model):
    nome = models.CharField(max_length=100)
    icon_solo = models.ImageField(upload_to='imagens/icon_solo/',null=True)
    def __str__(self):
        return self.nome

    
class PH(models.Model):
    nome = models.CharField(max_length=100)
    icon_PH = models.ImageField(upload_to='imagens/icon_PH/',null=True)
    def __str__(self):
        return self.nome
    
class Irrigacao(models.Model):
    nome = models.CharField(max_length=100)
    icon_irrigacao = models.ImageField(upload_to='imagens/icon_Irrigacao/',null=True)
    def __str__(self):
        return self.nome
class ExposicaoSolar(models.Model):
    nome = models.CharField(max_length=100)
    icon_exposicaosolar = models.ImageField(upload_to='imagens/icon_exposicao_solar/',null=True)
    def __str__(self):
        return self.nome


class Estacao(models.Model):
    nome = models.CharField(max_length=100)
    icon_estacao = models.ImageField(upload_to='imagens/icon_estacao/',null=True)
    def __str__(self):
        return self.nome



class Especies(models.Model):
    nome = models.CharField(max_length=100)
    nome_cientifico = models.CharField(max_length=100, null=True)
    detalhes = models.CharField(max_length=260, null=True)
    necessidade_solo = models.ForeignKey(Solo, on_delete=models.CASCADE)
    acidez_solo = models.ForeignKey(PH, on_delete=models.CASCADE)
    exposicao_solar = models.ForeignKey(ExposicaoSolar, on_delete=models.CASCADE)
    estacao_producao = models.ForeignKey(Estacao, on_delete=models.CASCADE)
    irrigacao = models.ForeignKey(Irrigacao, on_delete=models.CASCADE)
    imagem_especie = models.ImageField(upload_to='imagens/especies/',null=True)
    imagem_fruta = models.ImageField(upload_to='imagens/frutas/',null=True)
    
class EspeciesMinerais(models.Model):
    especie = models.ForeignKey(Especies, on_delete=models.CASCADE)
    mineral = models.ForeignKey(Minerais, on_delete=models.CASCADE)
    quantidade = models.CharField(max_length=100, null=True)

class Plantas(models.Model):
    especie = models.ForeignKey(Especies, on_delete=models.CASCADE)
    solo = models.ForeignKey(Solo, on_delete=models.CASCADE)
    exposicao_solar = models.CharField(max_length=100)
    estacao_producao = models.ForeignKey(Estacao, on_delete=models.CASCADE)
    irrigacao = models.ForeignKey(Irrigacao, on_delete=models.CASCADE)
    