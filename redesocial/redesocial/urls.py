
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('app_login.urls')),
    path('posts/', include('app_posts.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
