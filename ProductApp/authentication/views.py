from django.shortcuts import render, redirect,HttpResponse, reverse
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
# Create your views here.

from .forms import RegisterForm, LoginForm

def parseError(errors):
    errs = {}
    for (es, err) in errors.items():
        if es=='__all__' and err[0]=='Make sure passwords match':
            errs['passwordmatch'] = err[0]
        else:
            errs[es] = err[0]
    return errs

def storeUser(form):
    username = form.cleaned_data['username']
    firstname = form.cleaned_data['firstname']
    lastname = form.cleaned_data['lastname']
    password = form.cleaned_data['password1']
    email = form.cleaned_data['email']
    new_user = User(username=username, email=email, first_name=firstname, last_name=lastname)
    new_user.set_password(password)
    new_user.save()
    return new_user


class AuthenticationForm(View):
    template_name = 'authentication/form.html'
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request, self.template_name, context={'error':False})

authentication_form_view = AuthenticationForm.as_view()


class AuthRegister(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return redirect(reverse('auth:auth_form'))
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = RegisterForm(request.POST)
        if (form.is_valid()):
            user = storeUser(form)
            return render(request, 'authentication/form.html', {'error': False, 'registered': True})
        else:
            print({'error':True, 'errorsouce':'register', **parseError(form.errors)})
            return render(request, 'authentication/form.html',{'error':True, 'registererror':True, **parseError(form.errors)})
            

auth_register_view = AuthRegister.as_view()

class AuthLogin(View):
    def get(self, request):
        return redirect('auth:auth_form')
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(self.request, user)
                return redirect('home')
        return render(request, 'authentication/form.html', {'loginfailed': 'Invalid Credentials'})

auth_login_view = AuthLogin.as_view()
