from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import tilni_ozgartirish

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('tilni_ozgartirish/<str:til_kodi>/', tilni_ozgartirish, name='tilni_ozgartirish'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
