from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ResumeAPIView


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('post/', views.post, name='post'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('api/resume/', ResumeAPIView.as_view(), name='resume_api'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

