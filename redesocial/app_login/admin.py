from atexit import register
from django.contrib import admin
from .models import Perfil, Seguir
# Register your models here.

admin.site.register(Perfil)
admin.site.register(Seguir)
