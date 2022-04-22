from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,
                                   related_name='perfil_de_usuario')
    foto_de_perfil = models.ImageField(upload_to='foto_de_perfil',
                                       blank=True)
    descricao = models.TextField(blank=True)
    nome_completo = models.CharField(max_length=254, blank=True)
    data_nasc = models.DateField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.usuario}'
    
class Seguir(models.Model):
    #seguidor é o usuario logado
    seguidor = models.ForeignKey(User,on_delete=models.CASCADE, 
                                 related_name='seguidor')
    #seguindo é a pessoa que o usuario logado esta acompanhando
    seguindo = models.ForeignKey(User, on_delete=models.CASCADE, 
                              related_name='seguindo')


