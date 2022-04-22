from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, 
                              related_name='posts_do_autor')
    imagem = models.ImageField(upload_to='posts_imagens')
    titulo = models.CharField(max_length=254, blank=True)
    upload_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.titulo
    
    class Meta:
        ordering = ['-upload_data',]
        
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='curtidas_posts')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='curtidor')
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return '{}:{}'.format(self.usuario, self.post)
        
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comentarios_posts')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='comentador')
    texto = models.CharField(default="", max_length=2000)

    def __str__(self) -> str:
        return '{}:{}'.format(self.usuario, self.post)