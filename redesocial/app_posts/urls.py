from django.urls import path
from app_posts import views

app_name = 'app_posts'

urlpatterns = [
    #path('', views.index, name='index'),
    path('curtir/<pk>', views.curtir, name='curtir'),
    path('descurtir/<pk>', views.descurtir, name='descurtir'),
]
