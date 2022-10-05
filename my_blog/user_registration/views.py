from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# MVT - MVC (Djangoban MVT, mert a Template veszi át a Control szerepét)
#  register oldal
# 
# Create your views here.
# 1. létrehoztam a modelt -> az adatbázis része a fejlesztésnek
# 2. html
# 3. view, ami rendereli a html fájlunkat
# 4. login endpoint, URL

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your account has been created! You are able to login")
            # a login oldalra kellene irányítania
            # valamilyen visszajelzést kellene kapnom, hogy létrejött a userem

            return redirect('login')
    else:
        form = UserRegisterForm()
    
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context=context)