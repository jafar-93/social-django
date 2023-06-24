from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

class RegisterAccount(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'success register', 'success')
            return redirect('home:home')
        return render(request, 'account/register.html', {'form': form})

class LoginAccount(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'login success', 'success')
                return redirect('home:home')
            messages.error(request, 'username or password is wrong', 'warning')

        return render(request, self.template_name, {'form': form})

