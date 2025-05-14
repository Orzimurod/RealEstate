
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
        else:
            print("Username yoki parol noto'g'ri")
        return redirect(reverse_lazy('home'))
    elif request.method == 'GET':
        return render(request, 'login.html')


def register_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('login'))
        else:
            messages.add_message(request, messages.WARNING, form.errors)
    return render(request, 'register.html', {'form': form})
