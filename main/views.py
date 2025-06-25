from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm
from .models import Index, About, Resume, Projects,SocialMedia, Contact
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import ResumeSerializer
from django.shortcuts import get_object_or_404

from django.utils import translation

LANGUAGE_SESSION_KEY = 'django_language'

def tilni_ozgartirish(request, til_kodi):
    request.session[LANGUAGE_SESSION_KEY] = til_kodi
    translation.activate(til_kodi)
    response = redirect('/')
    response.set_cookie('django_language', til_kodi)
    return response



class ResumeAPIView(APIView):
    def get(self, request):
        resume = Resume.objects.all()
        serializer = ResumeSerializer(resume, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created_at')
    contact = Contact.objects.filter(status__title='active').first()
    social_links = SocialMedia.objects.filter(status__title='active')
    projects = Projects.objects.filter(status__title='active')
    index_data = Index.objects.filter(status__title="active").first()
    about_data = About.objects.filter(status__title="active").first()
    resume_list = Resume.objects.filter(status__title="active").order_by('-year')
    return render(request, 'main/index.html', {'index_data': index_data, 'about_data': about_data, 'resume_list': resume_list, 'projects': projects, 'social_links': social_links, 'contact': contact, 'posts': posts})

def footer(request):
    contact = Contact.objects.filter(status__title='active').first()
    social_links = SocialMedia.objects.filter(status__title='active')
    return render(request, 'main/footer.html', {'social_links': social_links, 'contact': contact})

def contact(request):
    contact = Contact.objects.filter(status__title='active').first()
    social_links = SocialMedia.objects.filter(status__title='active')
    index_data = Index.objects.filter(status__title="active").first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save()

            try:
                send_mail(
                    'Yangi xabar oldingiz!',
                    f"Ism: {message.name}\nEmail: {message.email}\n\n{message.message}",
                    f'{message.email}',
                    [settings.EMAIL_HOST_USER],
                )
            except Exception as e:
                print(e)


            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi!")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form, 'index_data': index_data, 'social_links': social_links, 'contact': contact})

def post(request):
    posts = Post.objects.all()
    return render(request, 'main/post.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    index_data = Index.objects.filter(status__title="active").first()
    return render(request, 'main/post_detail.html', {'post': post, 'index_data': index_data})