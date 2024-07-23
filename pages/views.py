
from projects.models import Project
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import ContactFormSubmission
from django.http import HttpResponse


def form_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        message = request.POST.get('message')
        if not name or not email or not message:
            return HttpResponse('All fields are required.', status=400)

        # ذخیره‌سازی در پایگاه داده
        ContactFormSubmission.objects.create(name=name, email=email, message=message,)

        return redirect('form_success')
    return HttpResponse('Invalid request method.')



def form_success(request):
    return render(request, 'pages/form_success.html')
def home(request):
    projects = Project.objects.all()
    return render(request, 'pages/home.html', {'projects': projects})


def about_me(request):
    return render(request, 'pages/aboutme.html')


def contact_me(request):
    return render(request, 'pages/contact me.html')
