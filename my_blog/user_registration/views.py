from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ProfileModel
from django.contrib.auth.models import User

# MVT - MVC (Djangoban MVT, mert a Template veszi át a Control szerepét)
#  register oldal
# 
# Create your views here.
# 1. létrehoztam a modelt -> az adatbázis része a fejlesztésnek
# 2. html
# 3. view, ami rendereli a html fájlunkat
# 4. login endpoint, URL

# function based views
# class based views

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # itt kell létrehoznom a profilt
            # username = form.cleaned_data.get('username')
            # usr_obj = User.objects.filter(username=username).first()

            # prof_temp = ProfileModel.objects.create(user_id=usr_obj.pk)

            messages.success(request, "Your account has been created! You are able to login")
            # a login oldalra kellene irányítania
            # valamilyen visszajelzést kellene kapnom, hogy létrejött a userem

            return redirect('login')
    else:
        form = UserRegisterForm()
    
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context=context)

# @login_required(login_url='login')
@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profilemodel)

        if u_form.is_valid() and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)

    context = {
        "u_form": u_form,
        "p_form": p_form
    }

    return render(request, 'user/profile.html', context=context)