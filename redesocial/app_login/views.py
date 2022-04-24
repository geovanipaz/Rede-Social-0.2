from http.client import HTTPResponse
from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import CriarPerfilForm, EditarPerfilForm
from .models import Seguir, User,Perfil
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app_posts.forms import CriarPostForm, CriarComentarioForm
from app_posts.models import Like, Post

# Create your views here.

def index(request):
    return render(request, 'app_login/index.html')

def criaUsuario(request):
    form = CriarPerfilForm()
    registrado = False
    if request.method == 'POST':
        form = CriarPerfilForm(data=request.POST)
        if form.is_valid():
            usuario = form.save()
            registrado = True
            usuario_perfil = Perfil(usuario=usuario)
            usuario_perfil.save()
            messages.success(request,'Usuário Criado com Sucesso.')
            return HttpResponseRedirect(reverse('app_login:login'))
    return render(request,'app_login/cadastrar.html',context={'form':form})

def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #password = request.POST['password']
            #username = request.POST['username']
            
            user = authenticate(username=username, password=password)
            if user is not None:
                
                auth.login(request,user)
                messages.success(request,'Login realizado com sucesso')
                return HttpResponseRedirect(reverse('app_login:perfil',
                                                    kwargs={'username':user.username}))
           
    return render(request, 'app_login/login.html',
                  context={'form':form})
    
@login_required    
def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_login:login'))

@login_required         
def perfil(request, username):
    context = {}
    if username == request.user.username:
        form_post = CriarPostForm()
        if request.method == 'POST':
            form_post = CriarPostForm(request.POST, request.FILES)
            if form_post.is_valid():
                post = form_post.save(commit=False)
                post.autor = request.user
                post.save()
                return HttpResponseRedirect(reverse(
                    'app_login:perfil', kwargs={'username': request.user.username}))
        outro_usuario = User.objects.get(username=username)
        context = {
            'proprio_perfil':True,
            'perfil':outro_usuario,
            'form_post':form_post,
        }
    else:
        outro_usuario = User.objects.get(username=username)
        ja_seguindo = Seguir.objects.filter(
            seguidor=request.user, seguindo=outro_usuario)
        context = {'perfil':outro_usuario}
        context.update({'ja_seguindo':ja_seguindo})
        
    return render(request, 'app_login/perfil.html', context)

@login_required
def editarperfil(request):
    perfil_atual = Perfil.objects.get(usuario=request.user)
    form = EditarPerfilForm(instance=perfil_atual)
    if request.method == 'POST':
        form = EditarPerfilForm(
            request.POST,
            request.FILES,
            instance=perfil_atual
        )
        if form.is_valid():
            form.save(commit=True)
            form = EditarPerfilForm(instance=perfil_atual)
            return HttpResponseRedirect(reverse('app_login:perfil',
                                                kwargs={'username':request.user.username}))
    return render(request, 'app_login/editarperfil.html',
                  context={'form':form})
 
@login_required   
def seguir(request, username):
    seguindo = User.objects.get(username=username)
    seguidor = request.user
    ja_seguido = Seguir.objects.filter(seguidor=seguidor, seguindo=seguindo)
    if not ja_seguido:
        usuario_seguido = Seguir(seguidor=seguidor, seguindo=seguindo)
        usuario_seguido.save()
    return HttpResponseRedirect(reverse('app_login:perfil',
                                        kwargs={'username':username}))

@login_required   
def deseguir(request, username):
    seguindo = User.objects.get(username=username)
    seguidor = request.user
    ja_seguido = Seguir.objects.filter(seguidor=seguidor, seguindo=seguindo)
    ja_seguido.delete()
    return HttpResponseRedirect(reverse('app_login:perfil',
                                        kwargs={'username':username}))
    
def feed(request):
    lista_seguindo = Seguir.objects.filter(seguidor=request.user)
    posts_lista = Post.objects.filter(autor__in=lista_seguindo.values_list('seguindo'))
    posts_curtidos = Like.objects.filter(usuario=request.user)
    lista_posts_curtidos = posts_curtidos.values_list('post',flat=True)
    context = {
        'posts_lista':posts_lista,
        'lista_posts_curtidos': lista_posts_curtidos,
    }
    
    return render(request, 'app_login/feed.html', context)


'''
def feed(request):
    try:
        todos_posts = Post.objects.all().order_by('upload_data')
    except Exception as e:
        print(e)
    comentario_form = CriarComentarioForm()
    username = request.user.username
    
    context = {
        'todos_posts': todos_posts,
        'comentario_form': comentario_form,
        'username':username
    }
    
    return render(request,'app_login/feed.html', context)
'''
  

    