from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .forms import LoginForm

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('secret')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def secret_view(request):
    return render(request, 'secret.html')
