from http.client import HTTPResponse
from pyexpat.errors import messages
from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import CriarPerfilForm, EditarPerfilForm
from .models import User,Perfil
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
                print(user,'passou para cá')
                auth.login(request,user)
                messages.success(request,'Login realizado com sucesso')
                return HttpResponseRedirect(reverse('app_login:perfil'))
           
    return render(request, 'app_login/login.html',
                  context={'form':form})
            
def perfil(request):
    return render(request, 'app_login/perfil.html')

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
            return HttpResponseRedirect(reverse('app_login:perfil'))
    return render(request, 'app_login/editarperfil.html',
                  context={'form':form})
    