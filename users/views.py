from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ExtendsUserCreationFrom
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = ExtendsUserCreationFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Votre compte a bien été enregistré {username}")
            return redirect('home')
    else:
        form = ExtendsUserCreationFrom()
    context = {'form': form}
    return render(request, "users/register.html", context)

def profile(request):
    return render(request, "users/profile.html")