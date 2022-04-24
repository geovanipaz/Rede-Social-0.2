from audioop import reverse
from django.shortcuts import render, HttpResponseRedirect
from .models import Post, Like, Comentario
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def curtir(request,pk):
    post = Post.objects.get(pk=pk)
    ja_curtido  = Like.objects.filter(user=request.user, post = post)
    if not ja_curtido:
        post_curtido = Like(user=request.user, post = post)
        post_curtido.save()
    return HttpResponseRedirect(reverse('app_login:feed'))

@login_required
def descurtir(request,pk):
    post = Post.objects.get(pk=pk)
    ja_curtido  = Like.objects.filter(user=request.user, post = post)
    ja_curtido.delete()
    return HttpResponseRedirect(reverse('app_login:feed'))

