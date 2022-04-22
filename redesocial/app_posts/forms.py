from dataclasses import fields
from .models import Post, Comentario
from django import forms


class CriarPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('imagem', 'titulo')
        
class CriarComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('texto',)
