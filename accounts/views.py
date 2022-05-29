from django.shortcuts import render


from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.contrib.auth.views import LoginView,LogoutView
from. import forms
from django.views.generic import (ListView,TemplateView,
                                  UpdateView,DetailView,
                                  CreateView,DeleteView,
                                  View,FormView)


# Create your views here.
class Base(TemplateView):
    template_name = 'base.html'


class About(TemplateView):
    template_name = 'about.html'


class SignUp(CreateView):
    form_class = forms.SignUp
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'


class Hello(TemplateView):
    template_name = 'hello.html'


class Bye(TemplateView):
    template_name = 'bye.html'