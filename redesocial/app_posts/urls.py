from django.urls import path
from app_login import views

app_name = 'app_posts'

urlpatterns = [
    path('', views.index, name='index')
]
