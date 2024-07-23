from django.urls import path
from .views import home
from . import views
from .views import form_submit, form_success

urlpatterns = [
    path('', home, name='home'),
    path('about-me/', views.about_me, name='about_me'),
    path('contact-me/', views.contact_me, name='contact-me'),
    path('form/', form_submit, name='form_submit'),
    path('form-success/', form_success, name='form_success'),
    path('form/success/', views.form_success, name='form_success'),
]